package com.mocloud.app.model

data class Message(
    val id: String,
    val sessionId: String,
    val role: Role,
    val content: String,
    val tokenCount: Int = 0,
    val sequenceNumber: Int,
    val createdAt: Long = 0L,
) {
    enum class Role { USER, ASSISTANT, TOOL }
}
