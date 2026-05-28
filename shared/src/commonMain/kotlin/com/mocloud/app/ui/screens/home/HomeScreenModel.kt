package com.mocloud.app.ui.screens.home

import cafe.adriel.voyager.core.model.ScreenModel
import cafe.adriel.voyager.core.model.screenModelScope
import com.mocloud.app.auth.supabase
import io.github.jan.supabase.auth.auth
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

sealed class HomeState {
    data object Active : HomeState()
    data object SignedOut : HomeState()
    data class Error(val message: String) : HomeState()
}

class HomeScreenModel : ScreenModel {

    private val _state = MutableStateFlow<HomeState>(HomeState.Active)
    val state = _state.asStateFlow()

    fun signOut() {
        screenModelScope.launch {
            try {
                supabase.auth.signOut()
                _state.value = HomeState.SignedOut
            } catch (e: Exception) {
                _state.value = HomeState.Error(e.message ?: "Sign out failed")
            }
        }
    }
}