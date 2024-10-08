package com.capstone;

import com.capstone.model.FoodItem;
import com.capstone.repository.FoodItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.util.Arrays;

@Component
public class DataLoader implements CommandLineRunner {

    @Autowired
    private FoodItemRepository foodItemRepository;

    @Override
    public void run(String... args) throws Exception {
        // Create some sample food items with correct constructor arguments
        FoodItem bread = new FoodItem(null, "Bread", 79, 2.7, 14.0, 1.0);
        FoodItem apple = new FoodItem(null, "Apple", 95, 0.5, 25.0, 0.3);
        FoodItem rice = new FoodItem(null, "Rice", 206, 4.3, 45.0, 0.4);
        FoodItem roti = new FoodItem(null, "Roti", 71, 2.7, 15.0, 0.4);
        FoodItem chocolate = new FoodItem(null, "Chocolate", 208, 2.2, 24.0, 12.0);
        FoodItem chips = new FoodItem(null, "Chips", 152, 2.0, 15.0, 10.0);
        FoodItem biscuits = new FoodItem(null, "Biscuits", 54, 0.8, 7.0, 2.4);
        FoodItem water = new FoodItem(null, "Water", 0, 0.0, 0.0, 0.0);
        FoodItem samosa = new FoodItem(null, "Samosa", 262, 6.0, 32.0, 13.0);
        FoodItem puff = new FoodItem(null, "Puff", 300, 5.0, 34.0, 17.0);


        // Save them to the database
        foodItemRepository.saveAll(Arrays.asList(bread, apple, rice, roti, chocolate, chips, biscuits, water, samosa, puff));
    }
}
