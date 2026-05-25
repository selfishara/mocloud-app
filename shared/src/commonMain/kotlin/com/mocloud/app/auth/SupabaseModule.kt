package com.mocloud.app.auth

import io.github.jan.supabase.SupabaseClient
import io.github.jan.supabase.auth.Auth
import io.github.jan.supabase.createSupabaseClient
import io.github.jan.supabase.postgrest.Postgrest

lateinit var supabase: SupabaseClient
    private set

fun initSupabase(url: String, anonKey: String) {
    supabase = createSupabaseClient(
        supabaseUrl = url,
        supabaseKey = anonKey,
    ) {
        install(Auth)
        install(Postgrest)
    }
}
