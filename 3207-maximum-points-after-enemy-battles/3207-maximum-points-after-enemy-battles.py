class Solution:
    def maximumPoints(self, enemyEnergies: list[int], currentEnergy: int) -> int:
        min_energy = min(enemyEnergies)
        
        # If we can't even defeat the smallest enemy once, we can never get >= 1 point
        if currentEnergy < min_energy:
            return 0
        
        # Absorb the energy of all enemies except the minimum one
        total_energy = currentEnergy + sum(enemyEnergies) - min_energy
        
        # Repeatedly defeat the smallest enemy with all accumulated energy
        return total_energy // min_energy