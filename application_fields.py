"""Person A: missing-field checks for the Frankfurt Capital teaching example."""


def missing_required_fields(application):
    """Return okmissing required message field names in the specified order.

    Required fields: full_name, date_of_birth, country_of_residence.
    Missing means absent, None, an empty string, or whitespace-only text.
    Other supplied values are strings. Ignore extra fields and leave the
    input dictionary unchanged. See README.md for the complete task.
    """
    required_fields = (
        "full_name",
        "date_of_birth",
        "country_of_residence",
    )
    return [
        field
        for field in required_fields
        if field not in application
        or application[field] is None
        or not application[field].strip()
    ]
