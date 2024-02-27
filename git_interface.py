from git import Repo, GitCommandError
import os

class GitInterface:
    def __init__(self):
        self.repo_path = None
        self.repo = None

    def clone_repository(self, repo_url, to_path):
        try:
            self.repo = Repo.clone_from(repo_url, to_path)
            self.repo_path = to_path
            return True, f"Repository cloned to {to_path}"
        except GitCommandError as e:
            return False, str(e)

    def create_branch(self, branch_name):
        if self.repo is None:
            return False, "Repository not initialized."
        try:
            new_branch = self.repo.create_head(branch_name)
            new_branch.checkout()
            return True, f"Branch '{branch_name}' created and checked out."
        except GitCommandError as e:
            return False, str(e)

    def checkout_branch(self, branch_name):
        if self.repo is None:
            return False, "Repository not initialized."
        try:
            self.repo.git.checkout(branch_name)
            return True, f"Checked out to branch '{branch_name}'."
        except GitCommandError as e:
            return False, str(e)

    def commit_changes(self, commit_message):
        if self.repo is None:
            return False, "Repository not initialized."
        try:
            self.repo.git.add(A=True)
            self.repo.git.commit('-m', commit_message)
            return True, "Changes committed."
        except GitCommandError as e:
            return False, str(e)

    def pull_updates(self):
        if self.repo is None:
            return False, "Repository not initialized."
        try:
            self.repo.git.pull()
            return True, "Repository updated."
        except GitCommandError as e:
            return False, str(e)

    def list_branches(self):
        if self.repo is None:
            return []
        return [str(b) for b in self.repo.branches]
