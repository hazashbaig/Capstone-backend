package com.capstone.repository;

import com.capstone.model.FoodItem;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.Optional;

public interface FoodItemRepository extends JpaRepository<FoodItem, Long> {

    // Case-insensitive search for the food item by name
    @Query("SELECT f FROM FoodItem f WHERE LOWER(f.name) = LOWER(:name)")
    Optional<FoodItem> findByNameIgnoreCase(@Param("name") String name);
}
