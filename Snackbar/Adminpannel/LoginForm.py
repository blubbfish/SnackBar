from wtforms import form, fields, validators
from Snackbar import db
from Snackbar.Models.Coffeeadmin import Coffeeadmin


class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    # noinspection PyUnusedLocal
    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid User')

        # we're comparing the plaintext pw with the the hash from the db
        if user.password != self.password.data:
            # to compare plain text passwords use
            # if User.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(Coffeeadmin).filter_by(name=self.login.data).first()
