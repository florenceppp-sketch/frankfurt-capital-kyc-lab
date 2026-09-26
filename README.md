# Frankfurt Capital: KYC Collaboration Lab

Financial Software Engineering · Session 7: Collaborative Software Development

Work in pairs to practise Git, pull requests and code reviews. Each person implements one small Python function on their own branch. You then review each other's work and merge both contributions.

This is a simplified teaching example using synthetic data. The functions do not perform identity verification or establish compliance with legal KYC requirements.

## What you need

- Python 3.9 or later, Git and VS Code
- A GitHub account for each person
- One shared GitHub repository per pair

No additional Python packages are required. A coding agent is optional. You must understand and explain any code you submit.

## Files

| File | Purpose |
|---|---|
| `application_fields.py` | Person A's function to implement |
| `document_status.py` | Person B's function to implement |
| `examples.py` | Synthetic inputs and expected results |
| `check_examples.py` | Runs the examples against your functions |
| `.gitignore` | Keeps local environment and cache files out of Git |

The two functions intentionally raise `NotImplementedError` until you implement them. The example checker reports these as **TODO**. This is the expected starting state.

## 1. Initialise and publish the repository

**Person A only:**

1. Extract the ZIP and open the inner `frankfurt-capital-kyc-lab` folder in VS Code. The README and Python files should be at the top level of the opened folder.
2. Open Source Control and choose **Initialize Repository**.
3. Inspect the files, including `.gitignore`. Stage the starter files and create the first commit, for example `Add KYC collaboration lab starter`.
4. Use **Publish to GitHub** to publish a **private** repository named `frankfurt-capital-kyc-lab`. Sign in if prompted. Use `main` as the shared branch name; if your initial branch has another name, rename it before continuing.
5. On GitHub, open the repository settings and invite Person B as a collaborator with access to contribute. Person B accepts the invitation.

If Git asks for your author name and email, configure them with your lecturer's help. You can use your GitHub-provided no-reply email address.

**Person B:** Clone this shared repository through VS Code's **Git: Clone** command or with `git clone <repository-url>`, then open the cloned folder.

Person A keeps using the original local folder. Do not publish a second repository from another copy of the ZIP. This archive contains no `.git` folder or existing Git history.

## 2. Create your branches

Both people start from the initial `main` branch. Use VS Code's branch menu or the terminal:

**Person A:**

```bash
git switch -c feature/application-fields
```

**Person B:**

```bash
git switch -c feature/document-status
```

Run `git status` or check the VS Code status bar to confirm your active branch before editing.

## 3. Implement your task

### Person A: missing application fields

Edit `application_fields.py` and implement `missing_required_fields(application)`.

Return a list of the missing required fields in this order:

1. `full_name`
2. `date_of_birth`
3. `country_of_residence`

A field is missing when its key is absent or its value is `None`, an empty string, or a string containing only whitespace. Assume all other supplied values are strings. Ignore extra fields and do not modify the input dictionary. Do not validate dates, country codes or identity documents.

For example, `{"full_name": "   ", "date_of_birth": "1998-04-12", "country_of_residence": "DE"}` should return `["full_name"]`.

### Person B: customer-facing document status

Edit `document_status.py` and implement `document_status_message(status)`.

Return the exact message for each status:

| Status | Message |
|---|---|
| `pending` | `Your document is awaiting review.` |
| `accepted` | `Your document has been accepted.` |
| `resubmit` | `Please submit a new document.` |
| Any other string | `Please contact support.` |

Assume the input is a string. Matching is case-sensitive. Do not strip whitespace or change case. Return the message rather than printing it inside the function.

### Working agreement

Keep your implementation in your assigned file. You may add one useful example to the corresponding example list in `examples.py`, but do not change existing expected results to make incorrect code pass. Editing the shared example file may require coordinating with your partner.

## 4. Run the examples

Open a terminal in the project folder. On macOS/Linux, use:

```bash
python3 check_examples.py fields
python3 check_examples.py status
```

Person A runs `fields`; Person B runs `status`. You can use `python` instead of `python3` if that is the Python 3 command on your system. On Windows, `py -3 check_examples.py fields` and `py -3 check_examples.py status` are alternatives.

Results:

- **PASS:** Your result matches the expected result.
- **FAIL:** Compare the expected and actual values shown.
- **TODO:** The function still contains its starter placeholder.
- **ERROR:** Your implementation raised another exception; read the reported error.

After both pull requests have been merged and you have updated your local `main`, run all examples:

```bash
python3 check_examples.py
```

The checker exits with status 0 only when every selected example passes. These examples support your review; they do not prove that every possible input has been covered.

## 5. Commit and push

1. Review your diff in VS Code.
2. Stage the files that belong to your change.
3. Commit with a meaningful message, such as `Add checks for missing application fields` or `Add customer messages for document status`.
4. Push/publish your feature branch to GitHub.

Copilot can suggest a commit message if available in your setup. Check it before using it and add missing context. It is not required for the lab.

## 6. Open a pull request

On GitHub, propose a pull request with `main` as the **base** and your feature branch as **compare**. Confirm that the diff contains the intended change. Request a review from your partner.

Suggested description:

```text
What changed?

Why is the change needed?

How did I check it?
```

Mention the examples you ran and any remaining uncertainty.

## 7. Review and respond

Each person reviews their partner's pull request:

- Does the implementation match the task?
- Are the examples relevant, including an edge case?
- Is the change understandable and focused?

Submit a specific comment and choose **Approve**, **Request changes**, or **Comment** as appropriate. Do not invent a defect if the code is correct. Explain what you checked when approving.

If a correction is needed, the author changes the code on the **same branch**, reruns the examples, commits and pushes again. The existing pull request updates automatically. Reply to the feedback and ask the reviewer to check again.

## 8. Merge and update

Once the partner has reviewed and the feedback is addressed, the author merges the pull request. This is our classroom agreement; GitHub does not enforce it unless repository rules have been configured.

After both contributions are merged, make sure your local work is committed and pushed, then:

```bash
git switch main
git pull
python3 check_examples.py
```

Both people should now see both completed functions on their local `main`.

## Completion check

Each person can show:

- Their feature branch, commit and merged pull request
- A review they submitted on their partner's contribution
- Passing examples for the combined result on local `main`
- An explanation of the difference between commit, push and merge

The lecturer demonstrates reverting changes and resolving merge conflicts separately.

## If you get stuck

- **Import/file not found:** Open the inner project folder and run the command from the folder containing `check_examples.py`.
- **Repository not accessible:** Check the invitation and that you are signed in with the invited GitHub account.
- **Push rejected:** Check the active branch and shared repository with your partner or lecturer. Do not force-push as a shortcut.
- **Unexpected files in Source Control:** Inspect them before staging. Keep passwords, tokens, real customer data and local environments out of Git.
- **Conflict:** Stop and understand both changes before choosing a result. Ask for help rather than discarding a partner's work.

Useful references: [Pro Git](https://git-scm.com/book/en/v2), [GitHub pull request reviews](https://docs.github.com/en/pull-requests/get-started/reviewing-pull-requests-quickstart).
