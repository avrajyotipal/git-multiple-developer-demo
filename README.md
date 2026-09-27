# Multi-Developer Git & GitHub Collaboration Workflow

A practical Git and GitHub project demonstrating how multiple developers collaborate on the same codebase using branches, remote repositories, cloning, fetching, pulling, pushing, Pull Requests, code reviews, and merging.

This project simulates a real-world development workflow using two developers:

* **Developer A** — Creates and manages the initial repository
* **Developer B** — Clones the repository, develops a feature on a separate branch, pushes the changes, creates a Pull Request, and participates in the review and merge process

> **Note:** This project is performed by one person using two separate local working directories to simulate two developers.

---

## 📌 Project Objective

The objective of this project is to understand and demonstrate a collaborative Git workflow from repository creation to feature development, Pull Request, code review, and merge.

The project covers:

* Local Git repository creation
* GitHub remote repository
* `git clone`
* `git remote`
* `git fetch`
* `git pull`
* Git branches
* Feature branch workflow
* `git add`
* `git commit`
* `git push`
* Pull Requests
* Code review
* Pull Request approval
* Branch merging
* Synchronizing the local repository after a merge

---

# 🏗️ Project Structure

```text
multi-developer-git-project/
│
├── app.py
├── README.md
└── requirements.txt
```

### `app.py`

Contains the Python application and the feature developed by Developer B.

### `README.md`

Project documentation and Git/GitHub workflow explanation.

### `requirements.txt`

Contains project dependencies.

---

# 👨‍💻 Developer Roles

## Developer A

Developer A is responsible for:

1. Creating the initial project
2. Initializing Git
3. Creating the first commit
4. Creating the GitHub repository
5. Connecting the local repository to GitHub
6. Pushing the `main` branch

## Developer B

Developer B is responsible for:

1. Cloning the remote repository
2. Fetching remote information
3. Pulling the latest `main` branch
4. Creating a feature branch
5. Implementing a new feature
6. Committing the changes
7. Pushing the feature branch
8. Creating a Pull Request
9. Participating in code review
10. Merging the approved changes into `main`

---

# 🔄 Overall Git Workflow

```text
                  GitHub Remote Repository
                           │
                           │
                    Developer A
                           │
                    Create Repository
                           │
                    Initial Commit
                           │
                       Push main
                           │
                           ▼
                    ┌─────────────┐
                    │     main    │
                    └─────────────┘
                           │
                           │ Clone
                           ▼
                    Developer B
                           │
                    git fetch
                           │
                    git pull
                           │
                           ▼
                Create Feature Branch
                           │
                 feature-calculator
                           │
                    Implement Feature
                           │
                       Commit
                           │
                       Push
                           │
                           ▼
                    Pull Request
                           │
                      Code Review
                           │
                       Approval
                           │
                         Merge
                           │
                           ▼
                    ┌─────────────┐
                    │     main    │
                    └─────────────┘
```

---

# 1️⃣ Developer A — Create the Initial Project

Create the project directory:

```bash
mkdir multi-developer-git-project
cd multi-developer-git-project
```

Create the required project files.

Initialize Git:

```bash
git init
```

Check the repository status:

```bash
git status
```

Add all project files:

```bash
git add .
```

Create the initial commit:

```bash
git commit -m "Initial project setup"
```

Rename the default branch to `main`:

```bash
git branch -M main
```

---

# 2️⃣ Create the GitHub Remote Repository

Create a new repository on GitHub:

```text
multi-developer-git-project
```

Connect the local repository to GitHub:

```bash
git remote add origin https://github.com/YOUR_USERNAME/multi-developer-git-project.git
```

Verify the remote:

```bash
git remote -v
```

Expected output:

```text
origin  https://github.com/YOUR_USERNAME/multi-developer-git-project.git (fetch)
origin  https://github.com/YOUR_USERNAME/multi-developer-git-project.git (push)
```

Here:

* `origin` is the name given to the remote repository.
* `fetch` represents downloading information from GitHub.
* `push` represents uploading local commits to GitHub.

---

# 3️⃣ Developer A — Push the Main Branch

Push the local `main` branch to GitHub:

```bash
git push -u origin main
```

The `-u` option establishes the upstream relationship between the local `main` branch and `origin/main`.

At this point, the initial project is available on GitHub.

---

# 4️⃣ Developer B — Clone the Repository

Developer B works from a separate directory to simulate a different developer's computer.

Move outside the original project:

```bash
cd ..
```

Create a directory for Developer B:

```bash
mkdir developer-b
cd developer-b
```

Clone the GitHub repository:

```bash
git clone https://github.com/YOUR_USERNAME/multi-developer-git-project.git
```

Enter the cloned repository:

```bash
cd multi-developer-git-project
```

Verify the remote:

```bash
git remote -v
```

The repository is now available in Developer B's local environment.

---

# 5️⃣ Developer B — Fetch Remote Changes

Developer B can retrieve information about remote branches and commits using:

```bash
git fetch origin
```

View all local and remote branches:

```bash
git branch -a
```

Example:

```text
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

## What does `git fetch` do?

`git fetch` downloads information from the remote repository without automatically merging those changes into the current working branch.

It is useful when a developer wants to inspect remote changes before integrating them.

---

# 6️⃣ Developer B — Pull the Latest Changes

Developer B makes sure the local `main` branch is up to date:

```bash
git pull origin main
```

## What does `git pull` do?

`git pull` performs two operations:

```text
git fetch
     +
git merge
```

It retrieves changes from the remote repository and integrates them into the current branch.

---

# 7️⃣ Create a Feature Branch

Developer B should not directly modify `main`.

Create a dedicated feature branch:

```bash
git checkout -b feature-calculator
```

Alternatively:

```bash
git switch -c feature-calculator
```

Verify the branches:

```bash
git branch
```

Expected:

```text
* feature-calculator
  main
```

The `*` indicates the currently active branch.

---

# 8️⃣ Implement the Feature

Developer B adds a calculator feature to `app.py`.

Example:

```python
def welcome_message():
    print("Welcome to the Multi-Developer Git Project!")


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    welcome_message()

    result = add_numbers(10, 20)
    print(f"10 + 20 = {result}")
```

Run the application:

```bash
python app.py
```

Expected output:

```text
Welcome to the Multi-Developer Git Project!
10 + 20 = 30
```

---

# 9️⃣ Commit the Feature

Check the working tree:

```bash
git status
```

Stage the modified file:

```bash
git add app.py
```

Create a commit:

```bash
git commit -m "Add calculator addition feature"
```

Check the commit history:

```bash
git log --oneline
```

---

# 🔟 Push the Feature Branch

Push the feature branch to GitHub:

```bash
git push -u origin feature-calculator
```

The GitHub repository now contains two branches:

```text
main
feature-calculator
```

The feature branch contains Developer B's changes while `main` remains unchanged.

---

# 1️⃣1️⃣ Create a Pull Request

Go to the GitHub repository.

Create a Pull Request with:

```text
Base branch:     main
Compare branch:  feature-calculator
```

Example Pull Request title:

```text
Add calculator addition feature
```

Example Pull Request description:

```text
## Changes

- Added add_numbers() function
- Added calculator example
- Tested the application locally

## Testing

The application was executed successfully using:

python app.py

## Review

Ready for code review.
```

The Pull Request requests that the changes from:

```text
feature-calculator
```

be merged into:

```text
main
```

---

# 1️⃣2️⃣ Code Review

The Pull Request should be reviewed before merging.

During the review:

* Inspect the changed files
* Review the implementation
* Check for potential issues
* Add comments if required
* Request changes if necessary
* Approve the Pull Request when satisfied

Example review comment:

```text
The calculator feature looks good. The implementation is simple and reusable.
The application was tested successfully.
```

After the review, approve the Pull Request.

---

# 1️⃣3️⃣ Merge the Pull Request

Once the Pull Request is approved:

1. Click **Merge pull request**
2. Confirm the merge
3. The feature branch changes are merged into `main`

The workflow becomes:

```text
feature-calculator
        │
        │ Pull Request
        ▼
      Review
        │
        │ Approval
        ▼
       main
```

---

# 1️⃣4️⃣ Synchronize Local Main

After the Pull Request has been merged, switch back to `main`:

```bash
git checkout main
```

Pull the latest changes:

```bash
git pull origin main
```

The local `main` branch now contains the calculator feature that was merged through GitHub.

Run the application again:

```bash
python app.py
```

Expected output:

```text
Welcome to the Multi-Developer Git Project!
10 + 20 = 30
```

---

# 🔍 Useful Git Commands

## Check repository status

```bash
git status
```

## View branches

```bash
git branch
```

## View local and remote branches

```bash
git branch -a
```

## View remote repositories

```bash
git remote -v
```

## View commit history

```bash
git log --oneline
```

## Visualize branch history

```bash
git log --oneline --graph --all
```

## Fetch remote changes

```bash
git fetch origin
```

## Pull remote changes

```bash
git pull origin main
```

## Push changes

```bash
git push
```

## Push a new branch

```bash
git push -u origin feature-calculator
```

---

# 📚 Git Concepts Demonstrated

| Concept        | Purpose                                 |
| -------------- | --------------------------------------- |
| `git init`     | Creates a local Git repository          |
| `git clone`    | Copies a remote repository locally      |
| `git remote`   | Manages remote repository connections   |
| `git fetch`    | Downloads remote repository information |
| `git pull`     | Fetches and integrates remote changes   |
| `git branch`   | Creates and manages branches            |
| `git checkout` | Switches branches                       |
| `git switch`   | Modern command for switching branches   |
| `git add`      | Stages changes                          |
| `git commit`   | Records changes in Git history          |
| `git push`     | Uploads commits to a remote repository  |
| Pull Request   | Proposes changes for review             |
| Code Review    | Examines proposed code changes          |
| Merge          | Integrates one branch into another      |

---

# 🎯 Learning Outcomes

After completing this project, the following Git and GitHub concepts should be understood:

* How local and remote repositories work
* How developers clone an existing repository
* Difference between `fetch` and `pull`
* How branches isolate feature development
* How developers push feature branches
* How Pull Requests facilitate collaboration
* How code reviews work
* How Pull Requests are approved
* How branches are merged
* How local repositories are synchronized after a merge
* How multiple developers can collaborate using Git and GitHub

---

# 🎥 YouTube Demonstration

The project is also documented through a YouTube video demonstrating the complete workflow.

The video covers:

1. Creating the initial repository
2. Creating the GitHub remote repository
3. Connecting local Git to GitHub
4. Pushing the `main` branch
5. Simulating Developer B
6. Cloning the repository
7. Understanding the remote repository
8. Using `git fetch`
9. Using `git pull`
10. Creating a feature branch
11. Implementing a feature
12. Committing changes
13. Pushing the feature branch
14. Creating a Pull Request
15. Performing a code review
16. Approving the Pull Request
17. Merging the Pull Request
18. Pulling the merged changes into the local `main` branch

---


# 👤 Developer Simulation

This project was completed by a single developer while simulating two developers using separate working directories:

```text
Developer A
    │
    └── Original local repository
              │
              ▼
        GitHub Repository
              │
              ▼
Developer B
    │
    └── Cloned local repository
```

This setup demonstrates the same fundamental Git workflow used when multiple developers work on a shared GitHub repository.

---

# 🏁 Final Workflow Summary

```text
Create Local Repository
          ↓
       git init
          ↓
      git commit
          ↓
 Create GitHub Repository
          ↓
    git remote add
          ↓
      git push main
          ↓
       Developer B
          ↓
       git clone
          ↓
       git fetch
          ↓
        git pull
          ↓
 Create Feature Branch
          ↓
 Implement Feature
          ↓
      git commit
          ↓
      git push
          ↓
    Pull Request
          ↓
     Code Review
          ↓
       Approval
          ↓
        Merge
          ↓
      git pull
          ↓
       Updated main
```

## Conclusion

This project demonstrates a complete collaborative Git and GitHub workflow, from initial repository creation through feature development, remote synchronization, Pull Request, code review, and final merge into the `main` branch.

It provides a practical simulation of how developers collaborate on software projects using Git and GitHub.
