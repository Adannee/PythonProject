{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8a7da32f-c6ec-4293-a4ca-dd601c8397de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: lxml in /opt/anaconda3/lib/python3.12/site-packages (5.2.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install lxml"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "086dcdfa-8a07-4ad0-b05a-da4fd34836b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3b11e408-29f1-4faf-becc-c5fc03fe9ebe",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://weworkremotely.com/categories/remote-programming-jobs\"\n",
    "headers = {\"User-Agent\": \"Mozilla/5.0\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "df0919cd-4ce4-4cf0-9c6b-7eb7a8869e12",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/cs/p50086m97m1d54jkbjqgggh80000gn/T/ipykernel_11345/4110262547.py:2: XMLParsedAsHTMLWarning: It looks like you're parsing an XML document using an HTML parser. If this really is an HTML document (maybe it's XHTML?), you can ignore or filter this warning. If it's XML, you should know that using an XML parser will be more reliable. To parse this document as XML, make sure you have the lxml package installed, and pass the keyword argument `features=\"xml\"` into the BeautifulSoup constructor.\n",
      "  soup = BeautifulSoup(response.text, \"lxml\")\n"
     ]
    }
   ],
   "source": [
    "response = requests.get(url, headers=headers)\n",
    "soup = BeautifulSoup(response.text, \"lxml\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "692c23b6-be2a-4aab-88ce-86e23de428fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "job_sections = soup.find_all(\"section\", class_=\"jobs\")\n",
    "jobs = []\n",
    "\n",
    "for section in job_sections:\n",
    "    for job in section.find_all(\"li\", class_=\"feature\"):\n",
    "        try:\n",
    "            company = job.find(\"span\", class_=\"company\").text.strip()\n",
    "            title = job.find(\"span\", class_=\"title\").text.strip()\n",
    "            region = job.find(\"span\", class_=\"region company\").text.strip()\n",
    "            link = \"https://weworkremotely.com\" + job.find(\"a\")[\"href\"]\n",
    "\n",
    "            jobs.append({\n",
    "                \"Title\": title,\n",
    "                \"Company\": company,\n",
    "                \"Location\": region,\n",
    "                \"Link\": link\n",
    "            })\n",
    "        except Exception as e:\n",
    "            continue\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "be73e046-a827-4ef8-9dfa-a7a7961eed9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Scraped 0 jobs from We Work Remotely\n"
     ]
    }
   ],
   "source": [
    "df = pd.DataFrame(jobs)\n",
    "df.to_csv(\"/Users/ivyadiele/Desktop/PythonProject/JobScraper/data/wwr_remote_jobs.csv\", index=False)\n",
    "\n",
    "print(f\"✅ Scraped {len(df)} jobs from We Work Remotely\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e52a369-eabc-4097-8093-74ad695a05c1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
