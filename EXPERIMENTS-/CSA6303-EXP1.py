def identify_threat_area(scenario):
    scenario = scenario.lower()

    areas = {
        "Banking Fraud Prevention":
            ["bank", "credit card", "transaction", "payment", "financial fraud"],

        "Healthcare Data Protection":
            ["hospital", "healthcare", "patient", "medical", "health data"],

        "E-Commerce Fraud Prevention":
            ["e-commerce", "online shopping", "customer", "shopping", "online payment"],

        "Cybersecurity / Network Protection":
            ["network", "malware", "phishing", "ransomware", "cyber attack"]
    }

    scores = {}

    for area, keywords in areas.items():
        scores[area] = sum(word in scenario for word in keywords)

    result = max(scores, key=scores.get)

    if scores[result] == 0:
        return "No relevant threat-intelligence area found."

    return result


scenario = input("Enter the business scenario: ")

result = identify_threat_area(scenario)

print("\nThreat Intelligence Application Area:", result)