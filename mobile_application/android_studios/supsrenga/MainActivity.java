package com.example.tvetern.supsrenga;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    // TO INFORMATION PAGE
    public void information(View view){
        Intent startInformationActivity = new Intent(this, DisplayInformation.class);
        startActivity(startInformationActivity);
    }

    // TO BOARD PAGE
    public void brettInformation(View view){
        Intent startBrettInformationActivity = new Intent(this, DisplayBrettInformation.class);
        startActivity(startBrettInformationActivity);
    }

    // TO RETURN PAGE
    public void tilbakeLevering(View view){
        Intent startReturnActivity = new Intent(this, Return.class);
        startActivity(startReturnActivity);
    }

    // TO ORDER PAGE
    public void orderPage(View view){
        Intent startOrderActivity = new Intent(this, Order.class);
        startActivity(startOrderActivity);
    }

    public void pricePage(View view){
        Intent startPriceActivity = new Intent(this, Price.class);
        startActivity(startPriceActivity);
    }
}
