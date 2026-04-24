        filtered_data_list.append(filtered_x)
        print(f"Merekam Skenario B... ({len(raw_data_list)}/{JUMLAH_SAMPEL})")

print("Perekaman selesai! Menampilkan grafik...")

plt.figure(figsize=(10, 5))
plt.plot(raw_data_list, label='Raw Data (Sinyal Mentah Kasar)', color='lightgray', linestyle='--')

if skenario_saat_ini == 'A':
    plt.plot(filtered_data_list, label='Filtered Cloud (Skenario A)', color='blue', linewidth=2)
    plt.title("Hasil Pengujian Skenario A (Cloud Computing)")
elif skenario_saat_ini == 'B':
    plt.plot(filtered_data_list, label='Filtered Edge (Skenario B)', color='red', linewidth=2)
    plt.title("Hasil Pengujian Skenario B (Edge Computing)")

plt.xlabel("Sampel Waktu")
plt.ylabel("Akselerasi (Sumbu X)")
plt.legend()
plt.grid(True)
plt.show()