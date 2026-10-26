"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Inspect successful and failed responses without using the network."""
    data = parse_json_response(200, fixture)
    assert data["lesson"] == 13
    print("Success response:", data)

    try:
        parse_json_response(500, b'{"error": "server problem"}')
    except ValueError as error:
        print("Handled error:", error)
    else:
        raise AssertionError("HTTP 500 should be rejected")


if __name__ == "__main__":
    main()
