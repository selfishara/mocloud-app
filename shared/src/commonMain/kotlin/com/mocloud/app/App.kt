package com.mocloud.app

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.mocloud.app.ui.theme.GhostWhite
import com.mocloud.app.ui.theme.MoCloudTheme

@Composable
@Preview
fun App() {
    MoCloudTheme {
        Box(
            modifier = Modifier.fillMaxSize(),
            contentAlignment = Alignment.Center,
        ) {
            Text("MoCloud", color = GhostWhite)
        }
    }
}
