from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from baserow.core.formula.field import FormulaField
from baserow.core.integrations.models import Integration
from baserow.core.services.models import Service

from .constants import BODY_TYPE, HTTP_METHOD


class SMTPIntegration(Integration):
    """
    Integration that stores SMTP server configuration. Can be used for sending emails.
    """

    host = models.CharField(
        max_length=255,
        help_text="The SMTP server hostname or IP address.",
    )
    port = models.PositiveIntegerField(
        default=587,
        help_text="The SMTP server port.",
    )
    use_tls = models.BooleanField(
        default=True,
        help_text="Whether to use TLS encryption.",
    )
    username = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The SMTP username for authentication.",
    )
    password = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The SMTP password for authentication.",
    )


class CoreHTTPRequestService(Service):
    """
    A service for handling HTTP requests.
    """

    http_method = models.CharField(
        max_length=10,
        choices=HTTP_METHOD.choices,
        default=HTTP_METHOD.GET,
        help_text="The HTTP method to use for the request (e.g., GET, POST).",
    )
    url = FormulaField(
        blank=True, help_text="The URL to which the HTTP request will be sent."
    )
    body_type = models.CharField(
        max_length=20,
        choices=BODY_TYPE.choices,
        default=BODY_TYPE.NONE,
        help_text="The type of the body content (e.g., JSON, Form Data).",
    )
    body_content = FormulaField(
        blank=True,
        help_text="The content of the body of the HTTP request.",
    )
    timeout = models.PositiveIntegerField(
        default=30,
        validators=[
            MinValueValidator(1, message="Value cannot be less than 1."),
            MaxValueValidator(120, message="Value cannot be greater than 120."),
        ],
        help_text="The timeout for the HTTP request in seconds.",
    )
    response_sample = models.JSONField(
        default=None,
        blank=True,
        null=True,
        help_text="Response got from test.",
    )


class CoreSMTPEmailService(Service):
    """
    A service for sending emails via SMTP.
    """

    from_email = FormulaField(
        help_text="The sender's email address.",
    )
    from_name = FormulaField(
        blank=True,
        help_text="The sender's name.",
    )
    to_emails = FormulaField(
        help_text="Comma-separated list of recipient email addresses.",
    )
    cc_emails = FormulaField(
        blank=True,
        help_text="Comma-separated list of CC email addresses.",
    )
    bcc_emails = FormulaField(
        blank=True,
        help_text="Comma-separated list of BCC email addresses.",
    )
    subject = FormulaField(
        help_text="The email subject.",
    )
    body_type = models.CharField(
        max_length=10,
        choices=[
            ("plain", "Plain Text"),
            ("html", "HTML"),
        ],
        default="plain",
        help_text="The type of the email body (plain text or HTML).",
    )
    body = FormulaField(
        help_text="The email body content.",
    )


class HTTPFormData(models.Model):
    """
    Model to store Form data.
    """

    service = models.ForeignKey(
        CoreHTTPRequestService, on_delete=models.CASCADE, related_name="form_data"
    )
    key = models.CharField(max_length=255, help_text="The form data key.")
    value = FormulaField(blank=True, help_text="The form data value.")


class HTTPHeader(models.Model):
    """
    Model to store HTTP headers.
    """

    service = models.ForeignKey(
        CoreHTTPRequestService, on_delete=models.CASCADE, related_name="headers"
    )
    key = models.CharField(max_length=255, help_text="The header key.")
    value = FormulaField(blank=True, help_text="The header value.")


class HTTPQueryParam(models.Model):
    """
    Model to store HTTP query parameters.
    """

    service = models.ForeignKey(
        CoreHTTPRequestService, on_delete=models.CASCADE, related_name="query_params"
    )
    key = models.CharField(max_length=255, help_text="The query parameter key.")
    value = FormulaField(blank=True, help_text="The query parameter value.")
