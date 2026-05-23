package com.mocloud.app.ui.screens.auth

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import cafe.adriel.voyager.core.screen.Screen
import cafe.adriel.voyager.core.model.rememberScreenModel
import cafe.adriel.voyager.navigator.LocalNavigator
import cafe.adriel.voyager.navigator.currentOrThrow
import com.mocloud.app.ui.screens.home.HomeScreen
import com.mocloud.app.ui.theme.*

class AuthScreen : Screen {

    @Composable
    override fun Content() {
        val navigator = LocalNavigator.currentOrThrow
        val screenModel = rememberScreenModel { AuthScreenModel() }
        val state by screenModel.state.collectAsState()

        LaunchedEffect(state) {
            if (state is AuthState.Success) {
                navigator.replace(HomeScreen())
            }
        }

        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(NearBlack)
                .safeContentPadding(),
            contentAlignment = Alignment.Center,
        ) {
            Column(
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.spacedBy(16.dp),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 32.dp),
            ) {
                Spacer(Modifier.weight(1f))

                // Logo / title
                Text(
                    text = "MoCloud",
                    fontSize = 48.sp,
                    fontWeight = FontWeight.Bold,
                    color = GhostWhite,
                )
                Text(
                    text = "Run AI agents from your phone.",
                    fontSize = 16.sp,
                    color = GhostWhite.copy(alpha = 0.6f),
                    textAlign = TextAlign.Center,
                )

                Spacer(Modifier.weight(1f))

                // Google button
                AuthButton(
                    text = "Continue with Google",
                    onClick = screenModel::signInWithGoogle,
                    enabled = state !is AuthState.Loading,
                    primary = true,
                )

                // Apple button
                AuthButton(
                    text = "Continue with Apple",
                    onClick = screenModel::signInWithApple,
                    enabled = state !is AuthState.Loading,
                    primary = false,
                )

                // Error message
                if (state is AuthState.Error) {
                    Text(
                        text = (state as AuthState.Error).message,
                        color = MaterialTheme.colorScheme.error,
                        fontSize = 13.sp,
                        textAlign = TextAlign.Center,
                    )
                }

                if (state is AuthState.Loading) {
                    CircularProgressIndicator(
                        color = Indigo,
                        modifier = Modifier.size(24.dp),
                    )
                }

                Spacer(Modifier.height(32.dp))

                Text(
                    text = "By continuing you agree to our Terms & Privacy Policy",
                    fontSize = 11.sp,
                    color = GhostWhite.copy(alpha = 0.35f),
                    textAlign = TextAlign.Center,
                )

                Spacer(Modifier.height(16.dp))
            }
        }
    }
}

@Composable
private fun AuthButton(
    text: String,
    onClick: () -> Unit,
    enabled: Boolean,
    primary: Boolean,
) {
    val shape = RoundedCornerShape(14.dp)
    if (primary) {
        Button(
            onClick = onClick,
            enabled = enabled,
            shape = shape,
            colors = ButtonDefaults.buttonColors(containerColor = Indigo),
            modifier = Modifier
                .fillMaxWidth()
                .height(52.dp),
        ) {
            Text(text, fontWeight = FontWeight.SemiBold, fontSize = 15.sp)
        }
    } else {
        OutlinedButton(
            onClick = onClick,
            enabled = enabled,
            shape = shape,
            border = androidx.compose.foundation.BorderStroke(1.dp, GhostWhite.copy(alpha = 0.2f)),
            colors = ButtonDefaults.outlinedButtonColors(contentColor = GhostWhite),
            modifier = Modifier
                .fillMaxWidth()
                .height(52.dp),
        ) {
            Text(text, fontWeight = FontWeight.SemiBold, fontSize = 15.sp)
        }
    }
}
