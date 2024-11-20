package com.capstone.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.io.BufferedReader;
import java.io.InputStreamReader;

@CrossOrigin(origins = {"http://localhost:3000", "https://capstone-six-silk.vercel.app"})
@RestController
@RequestMapping("/api")
public class PoseController {

    @GetMapping("/pose")
    public ResponseEntity<?> handlePoseEstimation() {
        try {
            // Run the Python script for pose estimation
            ProcessBuilder processBuilder = new ProcessBuilder("python", "C:\\Users\\hazas\\VIT\\Capstone\\backend\\NutritionAPI\\src\\main\\java\\com\\capstone\\controller\\ai_trainer.py");
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();

            // Capture the Python script output (pose estimation results)
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder result = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                result.append(line);
            }

            // Return the pose estimation results in the response
            return ResponseEntity.ok(result.toString());

        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error processing pose estimation");
        }
    }
}
