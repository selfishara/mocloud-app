package com.mocloud.app.ui.screens.home

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp
import cafe.adriel.voyager.core.screen.Screen
import com.mocloud.app.ui.theme.GhostWhite
import com.mocloud.app.ui.theme.Indigo
import com.mocloud.app.ui.theme.NearBlack

class HomeScreen : Screen {

    @Composable
    override fun Content() {
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(NearBlack),
            contentAlignment = Alignment.Center,
        ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
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
            }
        }
    }
}
