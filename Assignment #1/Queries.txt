SELECT mp.prescription_id, m.medication_id, COUNT(mp.patient_id) AS num_patients,
       CASE
          WHEN m.expiration_date < CURRENT_DATE THEN 'Expired'
          ELSE 'Active'
       END AS status
FROM medication_prescribed AS mp
JOIN medication AS m ON mp.medication_id = m.medication_id
GROUP BY m.medication_id

------------------------------------------------------------------------------------------------------------

SELECT d.doctor_id, w.name AS doctor_name, d.field, d.degree, dp.time, p.patient_id, p.name AS patient_name
FROM doctor AS d
JOIN worker AS w ON d.d_worker_id = w.worker_id
JOIN doctor_patient AS dp ON d.doctor_id = dp.doctor_id
JOIN patient AS p ON dp.patient_id = p.patient_id
WHERE p.age > 12 AND dp.time < '2022-01-01'
ORDER BY doctor_name DESC, p.name ASC
