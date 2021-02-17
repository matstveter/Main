package com.example.tvetern.supsrenga;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Price extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_price);
    }

    public void backToMain(View view){
        finish();
    }
}
