"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    Get("/react", "ReactDemoController@show"),
]

from masonite.auth import Auth 
ROUTES += Auth.routes()
