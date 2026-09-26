"""Person A: missing-field checks for the Frankfurt Capital teaching example."""


def missing_required_fields(application):
    """Return missing required field names in the specified order.

    Required fields: full_name, date_of_birth, country_of_residence.
    Missing means absent, None, an empty string, or whitespace-only text.
    Other supplied values are strings. Ignore extra fields and leave the
    input dictionary unchanged. See README.md for the complete task.
    """
    # TODO: Replace this placeholder with your implementation.
    required_fields = [
        "full_name",
        "date_of_birth",
        "country_of_residence",
    ]

    missing = []

    for field in required_fields:
        value = application.get(field)

        if value is None or value.strip() == "":
            missing.append(field)

    return missing
