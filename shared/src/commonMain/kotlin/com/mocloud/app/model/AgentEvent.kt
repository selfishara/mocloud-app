package com.mocloud.app.model

sealed class AgentEvent {
    data class Token(val text: String) : AgentEvent()
    data class ToolStart(val name: String, val inputJson: String) : AgentEvent()
    data class ToolOutput(val line: String) : AgentEvent()
    data class ToolEnd(val result: String, val durationMs: Long, val exitCode: Int) : AgentEvent()
    data class SessionEnd(val totalTokens: Int, val costUsd: Double) : AgentEvent()
    data class Error(val code: ErrorCode, val message: String) : AgentEvent()
    data class Usage(val tokens: Int, val estimatedCostUsd: Double) : AgentEvent()
}
