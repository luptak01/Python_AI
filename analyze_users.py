#!/usr/bin/env python3
"""
User Data Analysis Script

This script analyzes user data from the users.csv file and generates
a comprehensive analysis report in Markdown format.
"""

import csv
import statistics
from collections import Counter


def read_user_data(filename):
    """Read user data from CSV file and return list of dictionaries."""
    users = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users


def calculate_salary_stats(users):
    """Calculate salary statistics (min, max, average, median)."""
    salaries = [float(user['salary']) for user in users]
    return {
        'min': min(salaries),
        'max': max(salaries),
        'average': statistics.mean(salaries),
        'median': statistics.median(salaries)
    }


def get_occupation_distribution(users):
    """Get occupation distribution with counts."""
    occupations = [user['occupation'] for user in users]
    return Counter(occupations)


def generate_report(users, output_filename='user_analysis.md'):
    """Generate comprehensive analysis report in Markdown format."""
    
    # Calculate statistics
    salary_stats = calculate_salary_stats(users)
    occupation_dist = get_occupation_distribution(users)
    
    # Get column names
    columns = list(users[0].keys()) if users else []
    
    # Generate report content
    report = []
    report.append("# User Data Analysis Report\n")
    
    # Section 1: Data Summary
    report.append("## 1. Data Summary\n")
    report.append(f"**Total number of records:** {len(users)}\n")
    report.append("**Data columns:**\n")
    for col in columns:
        report.append(f"- {col}\n")
    report.append("\n")
    
    # Section 2: Salary Analysis
    report.append("## 2. Salary Analysis\n")
    report.append("**Salary Statistics:**\n")
    report.append(f"- **Minimum Salary:** ${salary_stats['min']:,.2f}\n")
    report.append(f"- **Maximum Salary:** ${salary_stats['max']:,.2f}\n")
    report.append(f"- **Average Salary:** ${salary_stats['average']:,.2f}\n")
    report.append(f"- **Median Salary:** ${salary_stats['median']:,.2f}\n")
    report.append("\n")
    
    # Section 3: Occupation Distribution
    report.append("## 3. Occupation Distribution\n")
    report.append("**Unique Occupations:** {}\n\n".format(len(occupation_dist)))
    report.append("| Occupation | Count |\n")
    report.append("|------------|-------|\n")
    
    # Sort occupations by count (descending) then by name
    for occupation, count in sorted(occupation_dist.items(), key=lambda x: (-x[1], x[0])):
        report.append(f"| {occupation} | {count} |\n")
    
    # Write report to file
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.writelines(report)
    
    print(f"✓ Analysis report generated successfully: {output_filename}")


def main():
    """Main function to run the analysis."""
    csv_filename = 'data/users.csv'
    
    print(f"Reading user data from {csv_filename}...")
    users = read_user_data(csv_filename)
    
    print(f"Analyzing {len(users)} user records...")
    generate_report(users)


if __name__ == '__main__':
    main()
