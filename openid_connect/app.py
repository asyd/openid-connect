from flask import Flask, flash, redirect, url_for
from flask_migrate import Migrate
from .extensions import db, auth
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata
from flask_debugtoolbar import DebugToolbarExtension


def create_app(environment: str):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(f"{environment}.py")
    app.config['OIDC'] = ProviderConfiguration(
        issuer=app.config['OIDC_PROVIDER']['issuer'],
        client_metadata=ClientMetadata(
            client_id=app.config['OIDC_PROVIDER']['client_id'],
            client_secret=app.config['OIDC_PROVIDER']['client_secret']
        )
    )

    if app.debug:
        toolbar = DebugToolbarExtension()
        toolbar.init_app(app)

    auth._provider_configurations = {'default': app.config['OIDC']}

    auth.init_app(app)

    db.init_app(app)
    Migrate(app, db)

    if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
        def _fk_pragma_on_connect(dbapi_con, con_record):  # noqa
            dbapi_con.execute('pragma foreign_keys=ON')

        with app.app_context():
            from sqlalchemy import event
            event.listen(db.engine, 'connect', _fk_pragma_on_connect)

    from .home import bp as ui_bp
    from .admin import bp as admin_bp

    app.register_blueprint(ui_bp)
    app.register_blueprint(admin_bp)

    @app.route('/ping')
    def ping():
        return 'pong'

    @app.route('/logout')
    @auth.oidc_logout
    def logout():
        flash("You've been successfully logout")
        return redirect(url_for('ui.hello'))

    return app
