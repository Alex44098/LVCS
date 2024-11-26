class PasswordController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_binds(self._bind, "password")
        self.password_is_ok = False

    def project_has_password(self):
        pass_project = self.model.password.get_password(self.model.current_project.info_id)
        if pass_project == "":
            return False
        return True

    def check_password(self):
        self.password_is_ok = False
        pass_entry = self.view.get_field("password_text")
        pass_project = self.model.password.get_password(self.model.current_project.info_id)
        if pass_entry.get() == pass_project:
            self.password_is_ok = True
        self.view.close_dialog()

    def _bind(self, frame):
        frame.apply_button.config(command=self.check_password)
