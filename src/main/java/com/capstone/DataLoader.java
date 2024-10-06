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
        FoodItem apple = new FoodItem(null, "Apple", 95, 0.5, 25.0, 0.3);
        FoodItem banana = new FoodItem(null, "Banana", 105, 1.3, 27.0, 0.3);
        FoodItem orange = new FoodItem(null, "Orange", 62, 1.2, 15.4, 0.2);

        // Save them to the database
        foodItemRepository.saveAll(Arrays.asList(apple, banana, orange));
    }
}
