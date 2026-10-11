
print("====================================")
print("       PHISHING EMAIL DETECTOR")
print("====================================")

# Step 1: Get the email message from the user
email = input("\nEnter the email message: ")

# Step 2: List suspicious words and phrases
suspicious_words = [
    "urgent",
    "password",
    "verify your account",
    "click here",
    "account suspended",
    "claim your prize"
]

# Step 3: List suspicious link patterns
suspicious_link_patterns = [
    "http://",
    "bit.ly/",
    "tinyurl.com/"
]

# Step 4: Convert the email to lowercase
email_lower = email.lower()

# Step 5: Prepare variables
found_words = []
found_links = []
risk_score = 0

# Step 6: Check for suspicious phrases
for word in suspicious_words:
    if word in email_lower:
        found_words.append(word)
        risk_score += 1

# Step 7: Check for suspicious link patterns
for pattern in suspicious_link_patterns:
    if pattern in email_lower:
        found_links.append(pattern)
        risk_score += 2

# Step 8: Display the analysis results
print("\n--- Email Analysis ---")

if found_words:
    print("Warning! Suspicious phrases found:")
    for word in found_words:
        print("-", word)
else:
    print("No listed suspicious phrases were found.")

if found_links:
    print("\nWarning! Suspicious link patterns found:")
    for link in found_links:
        print("-", link)
else:
    print("\nNo listed suspicious link patterns were found.")

# Step 9: Display the risk score
print("\nRisk Score:", risk_score)

# Step 10: Display the risk level
if risk_score == 0:
    print("Risk Level: Low")
elif risk_score <= 2:
    print("Risk Level: Medium")
else:
    print("Risk Level: High")

print("\nAnalysis complete.")
