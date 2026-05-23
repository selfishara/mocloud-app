package com.mocloud.app.model

enum class ErrorCode {
    TOOL_TIMEOUT,
    RATE_LIMITED,
    CONTEXT_TOO_LARGE,
    SANDBOX_UNAVAILABLE,
    AUTH_EXPIRED,
    QUOTA_EXCEEDED,
    INVALID_TOOL_CALL,
    BYOK_KEY_INVALID,
}
