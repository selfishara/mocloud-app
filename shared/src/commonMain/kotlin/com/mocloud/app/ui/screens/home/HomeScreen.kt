package com.mocloud.app.ui.screens.home

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import cafe.adriel.voyager.core.model.rememberScreenModel
import cafe.adriel.voyager.core.screen.Screen
import cafe.adriel.voyager.navigator.LocalNavigator
import cafe.adriel.voyager.navigator.currentOrThrow
import com.mocloud.app.ui.screens.auth.AuthScreen
import com.mocloud.app.ui.theme.ErrorRed
import com.mocloud.app.ui.theme.GhostWhite
import com.mocloud.app.ui.theme.Indigo
import com.mocloud.app.ui.theme.NearBlack

class HomeScreen : Screen {

    @Composable
    override fun Content() {
        val navigator = LocalNavigator.currentOrThrow
        val screenModel = rememberScreenModel { HomeScreenModel() }
        val state by screenModel.state.collectAsState()

        LaunchedEffect(state) {
            if (state is HomeState.SignedOut) {
                navigator.replace(AuthScreen())
            }
        }

        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(NearBlack),
            contentAlignment = Alignment.Center,
        ) {
            Column(
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.spacedBy(16.dp),
            ) {
                Text(
                    text = "MoCloud",
                    fontSize = 28.sp,
                    fontWeight = FontWeight.Bold,
                    color = GhostWhite,
                )
                Text(
                    text = "Home — coming soon",
                    fontSize = 14.sp,
                    color = Indigo,
                )
                Spacer(Modifier.height(32.dp))
                Button(
                    onClick = screenModel::signOut,
                    colors = ButtonDefaults.buttonColors(containerColor = ErrorRed),
                ) {
                    Text("Sign out", color = GhostWhite, fontWeight = FontWeight.SemiBold)
                }
                if (state is HomeState.Error) {
                    Text(
                        text = (state as HomeState.Error).message,
                        color = ErrorRed,
                        fontSize = 13.sp,
                    )
                }
            }
        }
    }
}