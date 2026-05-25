package com.mocloud.app

import androidx.compose.runtime.Composable
import androidx.compose.ui.tooling.preview.Preview
import cafe.adriel.voyager.navigator.Navigator
import cafe.adriel.voyager.transitions.SlideTransition
import com.mocloud.app.ui.screens.auth.AuthScreen
import com.mocloud.app.ui.theme.MoCloudTheme

@Composable
@Preview
fun App() {
    MoCloudTheme {
        Navigator(AuthScreen()) { navigator ->
            SlideTransition(navigator)
        }
    }
}
