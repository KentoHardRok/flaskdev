#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"
