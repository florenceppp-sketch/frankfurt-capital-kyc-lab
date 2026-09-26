"""Person B: status messages for the Frankfurt Capital teaching example."""


def document_status_message(status):
    """Return the customer message for a case-sensitive status string.

    Use the exact messages specified in README.md for pending, accepted
    and resubmit. For any other string, return the support message.
    """
    messages = {
        "pending": "Your document is awaiting review.",
        "accepted": "Your document has been accepted.",
        "resubmit": "Please submit a new document.",
    }
    return messages.get(status, "Please contact support.")
