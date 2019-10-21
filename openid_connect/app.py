from flask import Flask
from flask_migrate import Migrate
from .extensions import db
from .home import bp as ui_bp
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata
from flask_pyoidc import OIDCAuthentication


def create_app(environment: str):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(f"{environment}.py")

    db.init_app(app)
    Migrate(app, db)

    if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
        def _fk_pragma_on_connect(dbapi_con, con_record):  # noqa
            dbapi_con.execute('pragma foreign_keys=ON')

        with app.app_context():
            from sqlalchemy import event
            event.listen(db.engine, 'connect', _fk_pragma_on_connect)

    app.register_blueprint(ui_bp)

    app.config['OIDC'] = ProviderConfiguration(
        issuer=app.config['OIDC_PROVIDER']['issuer'],
        client_metadata=ClientMetadata(
            client_id=app.config['OIDC_PROVIDER']['client_id'],
            client_secret=app.config['OIDC_PROVIDER']['client_secret']
        )
    )

    app.auth = OIDCAuthentication({'default': app.config['OIDC']})
    app.auth.init_app(app)

    @app.route('/ping')
    def ping():
        return 'pong'

    return app
