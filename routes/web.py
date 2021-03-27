"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
]
# masonite-inertia demo routes
ROUTES += [
    Get("/inertia", "InertiaDemoController@show"),
    Get("/inertia-hello", "InertiaDemoController@hello"),
]
