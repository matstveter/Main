package com.example.tvetern.supsrenga;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class DisplayBrettInformation extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_brett_information);
    }

    public void backToMain(View view){
        finish();
    }

    public void orderPage(View view){
        Intent startOrderActivity = new Intent(this, Order.class);
        startActivity(startOrderActivity);
    }
}
