CPUUSD = float(input())
GPUUSD = float(input())
RAMUSD = float(input())
ramCount = int(input())
discountPercent = float(input())

transferBGNToUSD = 1.57

cpuPriceAfterDiscount = CPUUSD * (1 - discountPercent)
gpuPriceAfterDiscount = GPUUSD * (1 - discountPercent)
totalRamPrice = RAMUSD * ramCount

totalPriceUsd = cpuPriceAfterDiscount + gpuPriceAfterDiscount + totalRamPrice
total_price_bgn = totalPriceUsd * transferBGNToUSD

print(f"Money needed - {total_price_bgn:.2f} leva.")