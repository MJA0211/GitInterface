import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
# Assuming GitInterface is properly defined in git_interface.py
from git_interface import GitInterface

class GitGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Version System Control Git Interface")
        self.master.geometry("400x300")  # Set initial size of the window
        self.git_interface = GitInterface()

        # Use Notebook for tabbed interface
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both")

        # Tab 1: Repository operations
        self.repo_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.repo_tab, text="Repository")

        # Clone repository button
        self.clone_btn = ttk.Button(self.repo_tab, text="Clone Repository", command=self.clone_repo)
        self.clone_btn.pack(pady=10)

        # Create and Checkout branch in a single frame for layout purposes
        self.branch_frame = ttk.Frame(self.repo_tab)
        self.branch_frame.pack(fill="x", expand=True)

        self.create_branch_btn = ttk.Button(self.branch_frame, text="Create Branch", command=self.create_branch)
        self.create_branch_btn.pack(side="left", padx=5, expand=True)

        self.checkout_branch_btn = ttk.Button(self.branch_frame, text="Checkout Branch", command=self.checkout_branch)
        self.checkout_branch_btn.pack(side="right", padx=5, expand=True)

        # Commit changes button
        self.commit_btn = ttk.Button(self.repo_tab, text="Commit Changes", command=self.commit_changes)
        self.commit_btn.pack(pady=10)

        # Pull updates button
        self.pull_btn = ttk.Button(self.repo_tab, text="Pull Updates", command=self.pull_updates)
        self.pull_btn.pack(pady=10)

        # Tab 2: Branch operations
        self.branch_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.branch_tab, text="Branches")

        # Branch list with scrollbar
        self.branch_listbox_frame = ttk.Frame(self.branch_tab)
        self.branch_listbox_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.branch_scrollbar = ttk.Scrollbar(self.branch_listbox_frame)
        self.branch_scrollbar.pack(side="right", fill="y")

        self.branch_listbox = tk.Listbox(self.branch_listbox_frame, yscrollcommand=self.branch_scrollbar.set)
        self.branch_listbox.pack(side="left", fill="both", expand=True)
        self.branch_scrollbar.config(command=self.branch_listbox.yview)

        self.refresh_branch_list()

    def clone_repo(self):
        repo_url = simpledialog.askstring("Clone Repository", "Enter the repository URL:")
        to_path = simpledialog.askstring("Clone Repository", "Enter the target directory:")
        if repo_url and to_path:
            success, message = self.git_interface.clone_repository(repo_url, to_path)
            messagebox.showinfo("Clone Repository", message)
            if success:
                self.refresh_branch_list()

    def create_branch(self):
        branch_name = simpledialog.askstring("Create Branch", "Enter the new branch name:")
        if branch_name:
            success, message = self.git_interface.create_branch(branch_name)
            messagebox.showinfo("Create Branch", message)
            if success:
                self.refresh_branch_list()

    def checkout_branch(self):
        branch_name = simpledialog.askstring("Checkout Branch", "Enter the branch name to checkout:")
        if branch_name:
            success, message = self.git_interface.checkout_branch(branch_name)
            messagebox.showinfo("Checkout Branch", message)
            if success:
                self.refresh_branch_list()

    def commit_changes(self):
        commit_message = simpledialog.askstring("Commit Changes", "Enter the commit message:")
        if commit_message:
            success, message = self.git_interface.commit_changes(commit_message)
            messagebox.showinfo("Commit Changes", message)

    def pull_updates(self):
        success, message = self.git_interface.pull_updates()
        messagebox.showinfo("Pull Updates", message)
        if success:
            self.refresh_branch_list()

    def refresh_branch_list(self):
        self.branch_listbox.delete(0, tk.END)
        branches = self.git_interface.list_branches()
        for branch in branches:
            self.branch_listbox.insert(tk.END, branch)

if __name__ == "__main__":
    root = tk.Tk()
    app = GitGui(root)
    root.mainloop()