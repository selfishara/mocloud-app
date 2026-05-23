package com.mocloud.app.model

data class AgentSession(
    val id: String,
    val userId: String,
    val title: String,
    val totalTokens: Int = 0,
    val totalCostUsd: Double = 0.0,
    val createdAt: Long = 0L,
    val updatedAt: Long = 0L,
)
