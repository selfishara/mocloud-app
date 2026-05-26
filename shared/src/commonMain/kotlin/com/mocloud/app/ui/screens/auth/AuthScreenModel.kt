package com.mocloud.app.ui.screens.auth

import cafe.adriel.voyager.core.model.ScreenModel
import cafe.adriel.voyager.core.model.screenModelScope
import com.mocloud.app.auth.supabase
import io.github.jan.supabase.auth.auth
import io.github.jan.supabase.auth.providers.Apple
import io.github.jan.supabase.auth.providers.Google
import io.github.jan.supabase.auth.status.SessionStatus
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
sealed class AuthState {
    data object Idle : AuthState()
    data object Loading : AuthState()
    data object Success : AuthState()
    data class Error(val message: String) : AuthState()
}

class AuthScreenModel : ScreenModel {

    private val _state = MutableStateFlow<AuthState>(AuthState.Idle)
    val state = _state.asStateFlow()

    init {
        screenModelScope.launch {
            supabase.auth.sessionStatus.collect { status ->
                if (status is SessionStatus.Authenticated) {
                    _state.value = AuthState.Success
                }
            }
        }
    }
    fun signInWithGoogle() {
        screenModelScope.launch {
            _state.value = AuthState.Loading

            try {
                supabase.auth.signInWith(Google)
            } catch (e: Exception) {
                _state.value = AuthState.Error(e.message ?: "Google sign-in failed")
            }
        }
    }

    fun signInWithApple() {
        screenModelScope.launch {
            _state.value = AuthState.Loading
            try {
                supabase.auth.signInWith(Apple)

            } catch (e: Exception) {
                _state.value = AuthState.Error(e.message ?: "Apple sign-in failed")
            }
        }
    }
}
