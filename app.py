import os
from flask import Flask, jsonify, request


def create_app():
    """Create and configure the Flask app with multiple routes."""
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify(
            {
                "message": "cs504-ai Flask demo",
                "routes": ["/", "/health", "/info/<item>", "/echo"],
            }
        )

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"})

    @app.route("/info/<item>", methods=["GET"])
    def info(item):
        return jsonify({"item": item})

    @app.route("/echo", methods=["POST"])
    def echo():
        payload = request.get_json(silent=True) or {}
        return jsonify({"echo": payload})

    return app


if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
