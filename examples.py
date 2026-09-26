"""Synthetic inputs and expected results. No real customer data."""

# Each tuple contains: description, input, expected result.
FIELD_EXAMPLES = [
    (
        "Complete application",
        {
            "full_name": "Taylor Example",
            "date_of_birth": "1998-04-12",
            "country_of_residence": "DE",
        },
        [],
    ),
    (
        "Name contains only whitespace",
        {
            "full_name": "   ",
            "date_of_birth": "1998-04-12",
            "country_of_residence": "DE",
        },
        ["full_name"],
    ),
    (
        "Missing key, None and empty string",
        {"full_name": None, "country_of_residence": ""},
        ["full_name", "date_of_birth", "country_of_residence"],
    ),
    (
        "Tabs and newlines count as whitespace",
        {
            "full_name": "Taylor Example",
            "date_of_birth": "\t\n",
            "country_of_residence": "DE",
        },
        ["date_of_birth"],
    ),
    (
        "Ignore additional fields",
        {
            "full_name": "Taylor Example",
            "date_of_birth": "1998-04-12",
            "country_of_residence": "DE",
            "optional_note": None,
        },
        [],
    ),
]

STATUS_EXAMPLES = [
    ("Awaiting review", "pending", "Your document is awaiting review."),
    ("Accepted document", "accepted", "Your document has been accepted."),
    ("New document needed", "resubmit", "Please submit a new document."),
    ("Unknown status", "unknown", "Please contact support."),
    ("Empty status", "", "Please contact support."),
    ("Matching is case-sensitive", "Pending", "Please contact support."),
    ("Whitespace is not removed", " pending ", "Please contact support."),
]
