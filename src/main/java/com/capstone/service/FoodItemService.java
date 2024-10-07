package com.capstone.service;

import com.capstone.model.FoodItem;
import com.capstone.repository.FoodItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class FoodItemService {

    private final FoodItemRepository foodItemRepository;

    @Autowired
    public FoodItemService(FoodItemRepository foodItemRepository) {
        this.foodItemRepository = foodItemRepository;
    }

    public List<FoodItem> findAll() {
        return foodItemRepository.findAll();
    }

    public Optional<FoodItem> findById(Long id) {
        return foodItemRepository.findById(id);
    }

    public Optional<FoodItem> findByName(String name) {
        return foodItemRepository.findByNameIgnoreCase(name);
    }

    public FoodItem save(FoodItem foodItem) {
        return foodItemRepository.save(foodItem);
    }

    public void deleteById(Long id) {
        foodItemRepository.deleteById(id);
    }
}
