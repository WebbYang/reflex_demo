import reflex as rx

class WebappConfig(rx.Config):
    pass

config = WebappConfig(
    app_name="webapp",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    frontend_port=8050,
)