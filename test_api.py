
import requests

BASE_URL = "http://127.0.0.1:8000"


def run_test(name, method, endpoint, expected_status, **kwargs):
    print(f"\n--- {name} ---")

    response = requests.request(
        method,
        BASE_URL + endpoint,
        timeout=120,
        **kwargs
    )

    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == expected_status
    return response


if __name__ == "__main__":
    run_test("Home", "GET", "/", 200)

    health = run_test("Health", "GET", "/health", 200)
    assert health.json()["model_loaded"] is True

    positive = run_test(
        "Positive sentiment",
        "POST",
        "/predict",
        200,
        json={"text": "I absolutely love this movie!"}
    )
    assert positive.json()["sentiment"] == "POSITIVE"

    negative = run_test(
        "Negative sentiment",
        "POST",
        "/predict",
        200,
        json={"text": "This is the worst experience ever."}
    )
    assert negative.json()["sentiment"] == "NEGATIVE"

    run_test(
        "Empty input",
        "POST",
        "/predict",
        422,
        json={"text": ""}
    )

    run_test(
        "Missing text",
        "POST",
        "/predict",
        422,
        json={}
    )

    run_test(
        "Invalid input type",
        "POST",
        "/predict",
        422,
        json={"text": 123}
    )

    print("\nAll API tests passed!")
