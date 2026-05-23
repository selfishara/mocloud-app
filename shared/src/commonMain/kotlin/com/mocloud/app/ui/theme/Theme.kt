package com.mocloud.app.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

val Indigo = Color(0xFF6366F1)
val IndigoDark = Color(0xFF4338CA)
val Violet = Color(0xFFA78BFA)
val NearBlack = Color(0xFF0F0F12)
val Surface = Color(0xFF1A1A2E)
val GhostWhite = Color(0xFFF8F8FF)
val Cyan = Color(0xFF06B6D4)
val Emerald = Color(0xFF10B981)
val Amber = Color(0xFFF59E0B)
val ErrorRed = Color(0xFFEF4444)

private val DarkColors = darkColorScheme(
    primary = Indigo,
    onPrimary = GhostWhite,
    secondary = Violet,
    onSecondary = GhostWhite,
    background = NearBlack,
    onBackground = GhostWhite,
    surface = Surface,
    onSurface = GhostWhite,
    error = ErrorRed,
    onError = GhostWhite,
)

@Composable
fun MoCloudTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = DarkColors,
        content = content,
    )
}
