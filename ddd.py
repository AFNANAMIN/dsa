{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import re\n",
    "import matplotlib\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "\n",
    "import seaborn as sns\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.multiclass import OneVsRestClassifier\n",
    "\n",
    "import nltk\n",
    "from nltk.corpus import stopwords\n",
    "\n",
    "from sklearn.svm import LinearSVC\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.pipeline import Pipeline\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.feature_extraction.text import TfidfTransformer\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nltk.download() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stop_words = set(stopwords.words('english'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\D\\anaconda3\\envs\\py36\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3057: DtypeWarning: Columns (5) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  interactivity=interactivity, compiler=compiler, result=result)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv('data/Consumer_Complaints2.csv')\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date received</th>\n",
       "      <th>Product</th>\n",
       "      <th>Sub-product</th>\n",
       "      <th>Issue</th>\n",
       "      <th>Sub-issue</th>\n",
       "      <th>Consumer complaint narrative</th>\n",
       "      <th>Company public response</th>\n",
       "      <th>Company</th>\n",
       "      <th>State</th>\n",
       "      <th>ZIP code</th>\n",
       "      <th>Tags</th>\n",
       "      <th>Consumer consent provided?</th>\n",
       "      <th>Submitted via</th>\n",
       "      <th>Date sent to company</th>\n",
       "      <th>Company response to consumer</th>\n",
       "      <th>Timely response?</th>\n",
       "      <th>Consumer disputed?</th>\n",
       "      <th>Complaint ID</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>07/22/2019</td>\n",
       "      <td>Payday loan, title loan, or personal loan</td>\n",
       "      <td>Installment loan</td>\n",
       "      <td>Getting the loan</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>ONEMAIN FINANCIAL HOLDINGS, LLC.</td>\n",
       "      <td>CA</td>\n",
       "      <td>93015</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Postal mail</td>\n",
       "      <td>07/22/2019</td>\n",
       "      <td>In progress</td>\n",
       "      <td>Yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3314766</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>07/22/2019</td>\n",
       "      <td>Debt collection</td>\n",
       "      <td>I do not know</td>\n",
       "      <td>Written notification about debt</td>\n",
       "      <td>Didn't receive notice of right to dispute</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>United Debt Holdings, LLC</td>\n",
       "      <td>FL</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Web</td>\n",
       "      <td>07/22/2019</td>\n",
       "      <td>Closed with explanation</td>\n",
       "      <td>Yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3314276</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>07/22/2019</td>\n",
       "      <td>Student loan</td>\n",
       "      <td>Federal student loan servicing</td>\n",
       "      <td>Dealing with your lender or servicer</td>\n",
       "      <td>Trouble with how payments are being handled</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>AES/PHEAA</td>\n",
       "      <td>TX</td>\n",
       "      <td>787XX</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Web</td>\n",
       "      <td>07/22/2019</td>\n",
       "      <td>Closed with explanation</td>\n",
       "      <td>Yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3313762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>07/22/2019</td>\n",
       "      <td>Money transfer, virtual currency, or money ser...</td>\n",
       "      <td>Money order</td>\n",
       "      <td>Confusing or missing disclosures</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>MONEYGRAM PAYMENT SYSTEMS WORLDWIDE INC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Servicemember</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Web</td>\n",
       "      <td>07/22/2019</td>\n",
       "      <td>In progress</td>\n",
       "      <td>Yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3314557</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>07/22/2019</td>\n",
       "      <td>Mortgage</td>\n",
       "      <td>FHA mortgage</td>\n",
       "      <td>Trouble during payment process</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>FLAGSTAR BANK, FSB</td>\n",
       "      <td>NC</td>\n",
       "      <td>280XX</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Web</td>\n",
       "      <td>07/22/2019</td>\n",
       "      <td>In progress</td>\n",
       "      <td>Yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3314519</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Date received  ... Complaint ID\n",
       "0    07/22/2019  ...      3314766\n",
       "1    07/22/2019  ...      3314276\n",
       "2    07/22/2019  ...      3313762\n",
       "3    07/22/2019  ...      3314557\n",
       "4    07/22/2019  ...      3314519\n",
       "\n",
       "[5 rows x 18 columns]"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head() \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 69682 entries, 0 to 69681\n",
      "Data columns (total 18 columns):\n",
      "Date received                   69682 non-null object\n",
      "Product                         69682 non-null object\n",
      "Sub-product                     69682 non-null object\n",
      "Issue                           69682 non-null object\n",
      "Sub-issue                       61254 non-null object\n",
      "Consumer complaint narrative    2184 non-null object\n",
      "Company public response         34175 non-null object\n",
      "Company                         69682 non-null object\n",
      "State                           67510 non-null object\n",
      "ZIP code                        60013 non-null object\n",
      "Tags                            9415 non-null object\n",
      "Consumer consent provided?      21668 non-null object\n",
      "Submitted via                   69682 non-null object\n",
      "Date sent to company            69682 non-null object\n",
      "Company response to consumer    69682 non-null object\n",
      "Timely response?                69682 non-null object\n",
      "Consumer disputed?              0 non-null float64\n",
      "Complaint ID                    69682 non-null int64\n",
      "dtypes: float64(1), int64(1), object(16)\n",
      "memory usage: 9.6+ MB\n",
      "(69682, 18) None\n"
     ]
    }
   ],
   "source": [
    "print(df.shape, df.info() )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Consumer disputed?</th>\n",
       "      <th>Complaint ID</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>0.0</td>\n",
       "      <td>6.968200e+04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3.257706e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2.750156e+04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3.209777e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3.234079e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3.257454e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3.281195e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3.314766e+06</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Consumer disputed?  Complaint ID\n",
       "count                 0.0  6.968200e+04\n",
       "mean                  NaN  3.257706e+06\n",
       "std                   NaN  2.750156e+04\n",
       "min                   NaN  3.209777e+06\n",
       "25%                   NaN  3.234079e+06\n",
       "50%                   NaN  3.257454e+06\n",
       "75%                   NaN  3.281195e+06\n",
       "max                   NaN  3.314766e+06"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Date received', 'Product', 'Sub-product', 'Issue', 'Sub-issue',\n",
       "       'Consumer complaint narrative', 'Company public response', 'Company',\n",
       "       'State', 'ZIP code', 'Tags', 'Consumer consent provided?',\n",
       "       'Submitted via', 'Date sent to company', 'Company response to consumer',\n",
       "       'Timely response?', 'Consumer disputed?', 'Complaint ID'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "cols =['Date received', 'Product', 'Sub-product', 'Issue', 'Sub-issue',\n",
    "       'Consumer complaint narrative', 'Company public response', 'Company',\n",
    "       'State', 'ZIP code', 'Tags', 'Consumer consent provided?',\n",
    "       'Submitted via', 'Date sent to company', 'Company response to consumer',\n",
    "       'Timely response?', 'Consumer disputed?', 'Complaint ID']\n",
    "\n",
    "coltext = [  'Consumer complaint narrative' ]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "df[  'Consumer complaint narrative' ] = df[  'Consumer complaint narrative' ].fillna(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len( df[ df[  'Issue' ].isnull() ] )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Specifically, for each term in our dataset, we will calculate a measure called Term Frequency, Inverse Document Frequency, abbreviated to tf-idf. We will use sklearn.feature_extraction.text.TfidfVectorizer to calculate a tf-idf vector for each of consumer complaint narratives:\n",
    "sublinear_df is set to True to use a logarithmic form for frequency.\n",
    "min_df is the minimum numbers of documents a word must be present in to be kept.\n",
    "norm is set to l2, to ensure all our feature vectors have a euclidian norm of 1.\n",
    "ngram_range is set to (1, 2) to indicate that we want to consider both unigrams and bigrams.\n",
    "stop_words is set to \"english\" to remove all common pronouns (\"a\", \"the\", ...) to reduce the number of noisy features.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['text1'] = df[  'Issue' ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Consumer complaint narrative</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Product</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Checking or savings account</th>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Credit card or prepaid card</th>\n",
       "      <td>192</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Credit reporting, credit repair services, or other personal consumer reports</th>\n",
       "      <td>1005</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Debt collection</th>\n",
       "      <td>544</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Money transfer, virtual currency, or money service</th>\n",
       "      <td>43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mortgage</th>\n",
       "      <td>133</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Payday loan, title loan, or personal loan</th>\n",
       "      <td>39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Student loan</th>\n",
       "      <td>105</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Vehicle loan or lease</th>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                    Consumer complaint narrative\n",
       "Product                                                                         \n",
       "Checking or savings account                                                   85\n",
       "Credit card or prepaid card                                                  192\n",
       "Credit reporting, credit repair services, or ot...                          1005\n",
       "Debt collection                                                              544\n",
       "Money transfer, virtual currency, or money service                            43\n",
       "Mortgage                                                                     133\n",
       "Payday loan, title loan, or personal loan                                     39\n",
       "Student loan                                                                 105\n",
       "Vehicle loan or lease                                                         38"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Product').agg({ 'Consumer complaint narrative'  : \"count\"})\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Product_id'] = df['Product'].factorize()[0]   #label encoder !\n",
    "# df['Product_id'] \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "max_df corresponds to < documents than min_df",
     "output_type": "error",
     "traceback": [
      "Traceback \u001b[1;36m(most recent call last)\u001b[0m:\n",
      "  File \u001b[0;32m\"<ipython-input-34-386b2cd8c96c>\"\u001b[0m, line \u001b[0;32m7\u001b[0m, in \u001b[0;35m<module>\u001b[0m\n    features = tfidf.fit_transform(df[ coltext ] ).toarray()\n",
      "  File \u001b[0;32m\"C:\\D\\anaconda3\\envs\\py36\\lib\\site-packages\\sklearn\\feature_extraction\\text.py\"\u001b[0m, line \u001b[0;32m1652\u001b[0m, in \u001b[0;35mfit_transform\u001b[0m\n    X = super().fit_transform(raw_documents)\n",
      "\u001b[1;36m  File \u001b[1;32m\"C:\\D\\anaconda3\\envs\\py36\\lib\\site-packages\\sklearn\\feature_extraction\\text.py\"\u001b[1;36m, line \u001b[1;32m1075\u001b[1;36m, in \u001b[1;35mfit_transform\u001b[1;36m\u001b[0m\n\u001b[1;33m    \"max_df corresponds to < documents than min_df\")\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m\u001b[1;31m:\u001b[0m max_df corresponds to < documents than min_df\n"
     ]
    }
   ],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "\n",
    "tfidf = TfidfVectorizer(sublinear_tf=True, min_df=3, \n",
    "                        norm='l2', encoding='latin-1', \n",
    "                        ngram_range=(1, 2), stop_words='english')\n",
    "\n",
    "features = tfidf.fit_transform(df[ coltext ] ).toarray()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(69682, 8226)\n"
     ]
    }
   ],
   "source": [
    "count_vect = CountVectorizer()\n",
    "\n",
    "Xtext_count = count_vect.fit_transform(df[ coltext] ).toarray()\n",
    "\n",
    "print( Xtext.shape)\n",
    "\n",
    "tfidf_transformer = TfidfTransformer()\n",
    "Xtext_tfidf = tfidf_transformer.fit_transform(X_train_counts)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.57735027, 0.57735027, 0.57735027]])"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Xtext_tfidf.toarray()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "coltext = [ 'Issue']\n",
    "\n",
    "colselect  = coltext"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "from sklearn.svm import LinearSVC\n",
    "\n",
    "from sklearn.model_selection import cross_val_score\n",
    "\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(df[ 'Issue' ], \n",
    "                                                    df['Product'], random_state = 0)\n",
    "count_vect = CountVectorizer()\n",
    "X_train_counts = count_vect.fit_transform(X_train)\n",
    "tfidf_transformer = TfidfTransformer()\n",
    "X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)\n",
    "\n",
    "\n",
    "clf = LinearSVC().fit(X_train_tfidf, y_train)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product    Credit reporting, credit repair services, or o...\n",
      "Issue                   Incorrect information on your report\n",
      "Name: 10, dtype: object\n",
      "['Credit reporting, credit repair services, or other personal consumer reports']\n"
     ]
    }
   ],
   "source": [
    "print(df[[ 'Product', 'Issue' ]].iloc[10] )\n",
    "\n",
    "print(  clf.predict(count_vect.transform(df[coltext].iloc[10] ))) \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(52261, 169)"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_tfidf.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(69682,)"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[ 'Product' ].shape  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['product_id']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('LinearSVC', 0, 0.9786476868327402)\n",
      "('LinearSVC', 1, 0.9816877152698048)\n",
      "('LinearSVC', 2, 0.9814570296802342)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\D\\anaconda3\\envs\\py36\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:432: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n",
      "C:\\D\\anaconda3\\envs\\py36\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:469: FutureWarning: Default multi_class will be changed to 'auto' in 0.22. Specify the multi_class option to silence this warning.\n",
      "  \"this warning.\", FutureWarning)\n",
      "C:\\D\\anaconda3\\envs\\py36\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:432: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n",
      "C:\\D\\anaconda3\\envs\\py36\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:469: FutureWarning: Default multi_class will be changed to 'auto' in 0.22. Specify the multi_class option to silence this warning.\n",
      "  \"this warning.\", FutureWarning)\n",
      "C:\\D\\anaconda3\\envs\\py36\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:432: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n",
      "C:\\D\\anaconda3\\envs\\py36\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:469: FutureWarning: Default multi_class will be changed to 'auto' in 0.22. Specify the multi_class option to silence this warning.\n",
      "  \"this warning.\", FutureWarning)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('LogisticRegression', 0, 0.9786476868327402)\n",
      "('LogisticRegression', 1, 0.981630309988519)\n",
      "('LogisticRegression', 2, 0.9813996211033928)\n"
     ]
    }
   ],
   "source": [
    "X = df[ 'Issue' ]\n",
    "y = df[ 'Product' ]\n",
    "\n",
    "models = [\n",
    "    LinearSVC(),\n",
    "    LogisticRegression(random_state=0)\n",
    "]\n",
    "CV = 3\n",
    "cv_df = pd.DataFrame(index=range(CV * len(models)))\n",
    "entries = []\n",
    "for model in models:\n",
    "  model_name = model.__class__.__name__\n",
    "  accuracies = cross_val_score(model, \n",
    "                               X_train_tfidf.toarray(), \n",
    "                               y_train, \n",
    "                               scoring='accuracy', cv=CV)\n",
    "  for fold_idx, accuracy in enumerate(accuracies):\n",
    "    a = (model_name, fold_idx, accuracy)\n",
    "    entries.append(a)\n",
    "    print( a )\n",
    "cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>model_name</th>\n",
       "      <th>fold_idx</th>\n",
       "      <th>accuracy</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LinearSVC</td>\n",
       "      <td>0</td>\n",
       "      <td>0.978648</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LinearSVC</td>\n",
       "      <td>1</td>\n",
       "      <td>0.981688</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LinearSVC</td>\n",
       "      <td>2</td>\n",
       "      <td>0.981457</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LogisticRegression</td>\n",
       "      <td>0</td>\n",
       "      <td>0.978648</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LogisticRegression</td>\n",
       "      <td>1</td>\n",
       "      <td>0.981630</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>LogisticRegression</td>\n",
       "      <td>2</td>\n",
       "      <td>0.981400</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           model_name  fold_idx  accuracy\n",
       "0           LinearSVC         0  0.978648\n",
       "1           LinearSVC         1  0.981688\n",
       "2           LinearSVC         2  0.981457\n",
       "3  LogisticRegression         0  0.978648\n",
       "4  LogisticRegression         1  0.981630\n",
       "5  LogisticRegression         2  0.981400"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cv_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Consumer complaint narrative']"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "coltext"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Issue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Getting the loan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Written notification about debt</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Dealing with your lender or servicer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Confusing or missing disclosures</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Trouble during payment process</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Communication tactics</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Managing an account</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Written notification about debt</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Attempts to collect debt not owed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Problem with a credit reporting company's inve...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Written notification about debt</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>False statements or representation</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Written notification about debt</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Dealing with your lender or servicer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Threatened to contact someone or share informa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Managing an account</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Took or threatened to take negative or legal a...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Attempts to collect debt not owed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Improper use of your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Attempts to collect debt not owed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>False statements or representation</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Dealing with your lender or servicer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Problem when making payments</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Improper use of your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Trouble during payment process</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Attempts to collect debt not owed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Written notification about debt</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Attempts to collect debt not owed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69652</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69653</th>\n",
       "      <td>Dealing with your lender or servicer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69654</th>\n",
       "      <td>Attempts to collect debt not owed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69655</th>\n",
       "      <td>Unable to get your credit report or credit score</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69656</th>\n",
       "      <td>Improper use of your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69657</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69658</th>\n",
       "      <td>Attempts to collect debt not owed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69659</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69660</th>\n",
       "      <td>Managing an account</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69661</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69662</th>\n",
       "      <td>Managing an account</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69663</th>\n",
       "      <td>Struggling to pay your bill</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69664</th>\n",
       "      <td>Trouble during payment process</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69665</th>\n",
       "      <td>Attempts to collect debt not owed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69666</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69667</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69668</th>\n",
       "      <td>Problem when making payments</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69669</th>\n",
       "      <td>Fraud or scam</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69670</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69671</th>\n",
       "      <td>Problem with a credit reporting company's inve...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69672</th>\n",
       "      <td>Problem with a credit reporting company's inve...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69673</th>\n",
       "      <td>Problem with a credit reporting company's inve...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69674</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69675</th>\n",
       "      <td>Problems at the end of the loan or lease</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69676</th>\n",
       "      <td>Problem caused by your funds being low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69677</th>\n",
       "      <td>Trouble during payment process</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69678</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69679</th>\n",
       "      <td>Problem with a purchase shown on your statement</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69680</th>\n",
       "      <td>Incorrect information on your report</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69681</th>\n",
       "      <td>Problem with a purchase or transfer</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>69682 rows ﾃ・1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                   Issue\n",
       "0                                       Getting the loan\n",
       "1                        Written notification about debt\n",
       "2                   Dealing with your lender or servicer\n",
       "3                       Confusing or missing disclosures\n",
       "4                         Trouble during payment process\n",
       "5                                  Communication tactics\n",
       "6                                    Managing an account\n",
       "7                        Written notification about debt\n",
       "8                      Attempts to collect debt not owed\n",
       "9      Problem with a credit reporting company's inve...\n",
       "10                  Incorrect information on your report\n",
       "11                       Written notification about debt\n",
       "12                    False statements or representation\n",
       "13                       Written notification about debt\n",
       "14                  Dealing with your lender or servicer\n",
       "15     Threatened to contact someone or share informa...\n",
       "16                                   Managing an account\n",
       "17     Took or threatened to take negative or legal a...\n",
       "18                  Incorrect information on your report\n",
       "19                     Attempts to collect debt not owed\n",
       "20                           Improper use of your report\n",
       "21                     Attempts to collect debt not owed\n",
       "22                    False statements or representation\n",
       "23                  Dealing with your lender or servicer\n",
       "24                          Problem when making payments\n",
       "25                           Improper use of your report\n",
       "26                        Trouble during payment process\n",
       "27                     Attempts to collect debt not owed\n",
       "28                       Written notification about debt\n",
       "29                     Attempts to collect debt not owed\n",
       "...                                                  ...\n",
       "69652               Incorrect information on your report\n",
       "69653               Dealing with your lender or servicer\n",
       "69654                  Attempts to collect debt not owed\n",
       "69655   Unable to get your credit report or credit score\n",
       "69656                        Improper use of your report\n",
       "69657               Incorrect information on your report\n",
       "69658                  Attempts to collect debt not owed\n",
       "69659               Incorrect information on your report\n",
       "69660                                Managing an account\n",
       "69661               Incorrect information on your report\n",
       "69662                                Managing an account\n",
       "69663                        Struggling to pay your bill\n",
       "69664                     Trouble during payment process\n",
       "69665                  Attempts to collect debt not owed\n",
       "69666               Incorrect information on your report\n",
       "69667               Incorrect information on your report\n",
       "69668                       Problem when making payments\n",
       "69669                                      Fraud or scam\n",
       "69670               Incorrect information on your report\n",
       "69671  Problem with a credit reporting company's inve...\n",
       "69672  Problem with a credit reporting company's inve...\n",
       "69673  Problem with a credit reporting company's inve...\n",
       "69674               Incorrect information on your report\n",
       "69675           Problems at the end of the loan or lease\n",
       "69676             Problem caused by your funds being low\n",
       "69677                     Trouble during payment process\n",
       "69678               Incorrect information on your report\n",
       "69679    Problem with a purchase shown on your statement\n",
       "69680               Incorrect information on your report\n",
       "69681                Problem with a purchase or transfer\n",
       "\n",
       "[69682 rows x 1 columns]"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[ colselect]  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ain, test = train_test_split(df, random_state=42, test_size=0.33, shuffle=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pipeline = Pipeline([\n",
    "                ('tfidf', TfidfVectorizer(stop_words=stop_words)),\n",
    "                ('clf', OneVsRestClassifier(LinearSVC(), n_jobs=1)),\n",
    "            ])\n",
    "\n",
    "\n",
    "for category in categories:\n",
    "    print('... Processing {}'.format(category))\n",
    "    SVC_pipeline.fit(X_train, train[category])\n",
    "    pred = SVC_pipeline.predict(X_test)\n",
    "    print('Test accuracy is {}'.format(accuracy_score(test[category], pred)))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "models = [\n",
    "    RandomForestClassifier(n_estimators=10, max_depth=3, random_state=0),\n",
    "    LinearSVC(),\n",
    "    MultinomialNB(),\n",
    "    LogisticRegression(random_state=0),\n",
    "]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tfidf_transformer = TfidfTransformer()\n",
    "X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 5)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "features.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.4472136, 0.4472136, 0.4472136, 0.4472136, 0.4472136]])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "labels = df.category_id"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df = df[pd.notnull(df['Consumer complaint narrative'])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 4569 entries, 1 to 21662\n",
      "Data columns (total 18 columns):\n",
      "Date received                   4569 non-null object\n",
      "Product                         4569 non-null object\n",
      "Sub-product                     3106 non-null object\n",
      "Issue                           4569 non-null object\n",
      "Sub-issue                       2294 non-null object\n",
      "Consumer complaint narrative    4569 non-null object\n",
      "Company public response         2220 non-null object\n",
      "Company                         4569 non-null object\n",
      "State                           4556 non-null object\n",
      "ZIP code                        4556 non-null object\n",
      "Tags                            770 non-null object\n",
      "Consumer consent provided?      4569 non-null object\n",
      "Submitted via                   4569 non-null object\n",
      "Date sent to company            4569 non-null object\n",
      "Company response to consumer    4569 non-null object\n",
      "Timely response?                4569 non-null object\n",
      "Consumer disputed?              4568 non-null object\n",
      "Complaint ID                    4569 non-null float64\n",
      "dtypes: float64(1), object(17)\n",
      "memory usage: 678.2+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "col = ['Product', 'Consumer complaint narrative']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Complaint ID', 'Product', 'Sub-product', 'Issue', 'Sub-issue', 'State',\n",
       "       'ZIP code', 'Submitted via', 'Date received', 'Date sent to company',\n",
       "       'Company', 'Company response', 'Timely response?',\n",
       "       'Consumer disputed?'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Consumer disputed?</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Product</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Bank account or service</th>\n",
       "      <td>35775</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Consumer loan</th>\n",
       "      <td>8395</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Credit card</th>\n",
       "      <td>39478</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Credit reporting</th>\n",
       "      <td>34212</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Debt collection</th>\n",
       "      <td>37862</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Money transfers</th>\n",
       "      <td>1325</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mortgage</th>\n",
       "      <td>117720</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Payday loan</th>\n",
       "      <td>1211</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Student loan</th>\n",
       "      <td>8756</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         Consumer disputed?\n",
       "Product                                    \n",
       "Bank account or service               35775\n",
       "Consumer loan                          8395\n",
       "Credit card                           39478\n",
       "Credit reporting                      34212\n",
       "Debt collection                       37862\n",
       "Money transfers                        1325\n",
       "Mortgage                             117720\n",
       "Payday loan                            1211\n",
       "Student loan                           8756"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Product').agg({ 'Consumer disputed?' : \"count\"})\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Product', 'Consumer complaint narrative'], dtype='object')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df.columns = ['Product', 'Consumer_complaint_narrative']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df['category_id'] = df['Product'].factorize()[0]\n",
    "from io import StringIO\n",
    "category_id_df = df[['Product', 'category_id']].drop_duplicates().sort_values('category_id')\n",
    "category_to_id = dict(category_id_df.values)\n",
    "id_to_category = dict(category_id_df[['category_id', 'Product']].values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>Consumer_complaint_narrative</th>\n",
       "      <th>category_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Credit reporting</td>\n",
       "      <td>I have outdated information on my credit repor...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>I purchased a new car on XXXX XXXX. The car de...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Credit reporting</td>\n",
       "      <td>An account on my credit report has a mistaken ...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>This company refuses to provide me verificatio...</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>This complaint is in regards to Square Two Fin...</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Product                       Consumer_complaint_narrative  \\\n",
       "1   Credit reporting  I have outdated information on my credit repor...   \n",
       "2      Consumer Loan  I purchased a new car on XXXX XXXX. The car de...   \n",
       "7   Credit reporting  An account on my credit report has a mistaken ...   \n",
       "12   Debt collection  This company refuses to provide me verificatio...   \n",
       "16   Debt collection  This complaint is in regards to Square Two Fin...   \n",
       "\n",
       "    category_id  \n",
       "1             0  \n",
       "2             1  \n",
       "7             0  \n",
       "12            2  \n",
       "16            2  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\nREREDyWBR0RE9FASeERERA8lgUdERPRQEnhEREQPJYFHRET0UBJ4REREDyWBR0RE9FASeERERA8l\ngUdERPRQEnhEREQPJYFHRET0UBJ4REREDyWBR0RE9FASeERERA8lgUdERPRQEnhEREQPJYFHRET0\nUBJ4REREDyWBR0RE9FASeERERA8lgUdERPRQEnhEREQPJYFHRET0UBJ4REREDyWBR0RE9FASeERE\nRA8lgUdERPRQEnhEREQPJYFHRET0UBJ4REREDyWBR0RE9FASeERERA8lgUdERPTQlBK4pPUlfVPS\nFZIul/R0SRtIOlXSlfXzQ+pzJelQSVdJukjSdtPzT4iIiFj5TPUK/NPAybYfB2wNXA4cCJxmewvg\ntLoNsDOwRf3YDzhsiu8dERGx0lruBC5pXeDZwFEAtu+2fSuwOzC7Pm02sEf9enfgyy7OAtaX9Mjl\njjwiImIlNpUr8M2A+cCXJJ0v6UhJawOPsH0DQP388Pr8jYDrhl4/r+6LiIiIB2gqCXwGsB1wmO1t\ngT+yYLh8Mppknxd5krSfpLmS5s6fP38K4UVERIyvqSTwecA822fX7W9SEvpvB0Pj9fONQ8/fZOj1\nGwPXT/ymtg+3vb3t7WfOnDmF8CIiIsbXcidw278BrpO0Zd21E3AZcCKwd923N3BC/fpE4HV1NvoO\nwG2DofaIiIh4YGZM8fX7A0dLWh24GtiHclLwdUn7Ar8C9qzP/R6wC3AVcEd9bkRERCyHKSVw2xcA\n20/y0E6TPNfAW6byfhEREVGkEltEREQPJYFHRET0UBJ4REREDyWBR0RE9FASeERERA8lgUdERPRQ\nEnhEREQPJYFHRET0UBJ4REREDyWBR0RE9NBUa6FHj8w68KRp+17XHLLrtH2viIh44HIFHhER0UNJ\n4BERET2UBB4REdFDSeARERE9lAQeERHRQ0ngERERPZQEHhER0UNJ4BERET2UBB4REdFDSeARERE9\nlAQeERHRQ0ngERERPZQEHhER0UNJ4BERET2UBB4REdFDSeARERE9lAQeERHRQ0ngERERPZQEHhER\n0UNJ4BERET2UBB4REdFDSeARERE9lAQeERHRQ0ngERERPZQEHhER0UNJ4BERET2UBB4REdFDSeAR\nERE9lAQeERHRQ0ngERERPZQEHhER0UNJ4BERET2UBB4REdFDSeARERE9lAQeERHRQzNaBzAdZh14\n0rR8n2sO2XVavk9ERMSKlivwiIiIHppyApe0qqTzJX23bj9a0tmSrpR0rKTV6/4H1e2r6uOzpvre\nERERK6vpuAJ/G3D50PaHgU/a3gK4Bdi37t8XuMX25sAn6/MiIiJiOUwpgUvaGNgVOLJuC3ge8M36\nlNnAHvXr3es29fGd6vMjIiLiAZrqFfingHcDf67bDwVutX1v3Z4HbFS/3gi4DqA+flt9/kIk7Sdp\nrqS58+fPn2J4ERER42m5E7ikvwZutH3u8O5JnupleGzBDvtw29vb3n7mzJnLG15ERMRYm8oysmcC\nu0naBVgDWJdyRb6+pBn1Kntj4Pr6/HnAJsA8STOA9YCbp/D+ERERK63lvgK3/V7bG9ueBbwa+KHt\nvwXmAK+oT9sbOKF+fWLdpj7+Q9uLXIFHRETE0q2IdeDvAQ6QdBXlHvdRdf9RwEPr/gOAA1fAe0dE\nRKwUpqUSm+3TgdPr11cDT53kOXcBe07H+0VERKzsUoktIiKih5LAIyIieigJPCIiooeSwCMiInoo\nCTwiIqKHksAjIiJ6KAk8IiKih5LAIyIieigJPCIiooeSwCMiInooCTwiIqKHksAjIiJ6KAk8IiKi\nh5LAIyIiemha2olGRERMh1kHnjQt3+eaQ3adlu/TZbkCj4iI6KEk8IiIiB5KAo+IiOihJPCIiIge\nSgKPiIjooSTwiIiIHkoCj4iI6KEk8IiIiB5KAo+IiOihJPCIiIgeSgKPiIjooSTwiIiIHkoCj4iI\n6KEk8IiIiB5KAo+IiOihJPCIiIgemtE6gHGVpvQREbEi5Qo8IiKih5LAIyIieigJPCIiooeSwCMi\nInooCTwiIqKHksAjIiJ6KAk8IiKih5LAIyIieigJPCIiooeSwCMiInooCTwiIqKHksAjIiJ6KAk8\nIiKih5LAIyIieigJPCIiooeWO4FL2kTSHEmXS7pU0tvq/g0knSrpyvr5IXW/JB0q6SpJF0nabrr+\nERERESubqVyB3wu80/bjgR2At0h6AnAgcJrtLYDT6jbAzsAW9WM/4LApvHdERMRKbbkTuO0bbJ9X\nv74duBzYCNgdmF2fNhvYo369O/BlF2cB60t65HJHHhERsRKblnvgkmYB2wJnA4+wfQOUJA88vD5t\nI+C6oZfNq/siIiLiAZpyApe0DvAt4O22f7+kp06yz5N8v/0kzZU0d/78+VMNLyIiYixNKYFLWo2S\n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\nSUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7f72dd798160>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "fig = plt.figure(figsize=(8,6))\n",
    "df.groupby('Product').Consumer_complaint_narrative.count().plot.bar(ylim=0)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4569, 12633)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "\n",
    "tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')\n",
    "\n",
    "features = tfidf.fit_transform(df.Consumer_complaint_narrative).toarray()\n",
    "labels = df.category_id\n",
    "features.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "# 'Bank account or service':\n",
      "  . Most correlated unigrams:\n",
      "       . bank\n",
      "       . overdraft\n",
      "  . Most correlated bigrams:\n",
      "       . overdraft fees\n",
      "       . checking account\n",
      "# 'Consumer Loan':\n",
      "  . Most correlated unigrams:\n",
      "       . car\n",
      "       . vehicle\n",
      "  . Most correlated bigrams:\n",
      "       . vehicle xxxx\n",
      "       . toyota financial\n",
      "# 'Credit card':\n",
      "  . Most correlated unigrams:\n",
      "       . citi\n",
      "       . card\n",
      "  . Most correlated bigrams:\n",
      "       . annual fee\n",
      "       . credit card\n",
      "# 'Credit reporting':\n",
      "  . Most correlated unigrams:\n",
      "       . experian\n",
      "       . equifax\n",
      "  . Most correlated bigrams:\n",
      "       . trans union\n",
      "       . credit report\n",
      "# 'Debt collection':\n",
      "  . Most correlated unigrams:\n",
      "       . collection\n",
      "       . debt\n",
      "  . Most correlated bigrams:\n",
      "       . collect debt\n",
      "       . collection agency\n",
      "# 'Money transfers':\n",
      "  . Most correlated unigrams:\n",
      "       . wu\n",
      "       . paypal\n",
      "  . Most correlated bigrams:\n",
      "       . western union\n",
      "       . money transfer\n",
      "# 'Mortgage':\n",
      "  . Most correlated unigrams:\n",
      "       . modification\n",
      "       . mortgage\n",
      "  . Most correlated bigrams:\n",
      "       . mortgage company\n",
      "       . loan modification\n",
      "# 'Other financial service':\n",
      "  . Most correlated unigrams:\n",
      "       . dental\n",
      "       . passport\n",
      "  . Most correlated bigrams:\n",
      "       . help pay\n",
      "       . stated pay\n",
      "# 'Payday loan':\n",
      "  . Most correlated unigrams:\n",
      "       . borrowed\n",
      "       . payday\n",
      "  . Most correlated bigrams:\n",
      "       . big picture\n",
      "       . payday loan\n",
      "# 'Prepaid card':\n",
      "  . Most correlated unigrams:\n",
      "       . serve\n",
      "       . prepaid\n",
      "  . Most correlated bigrams:\n",
      "       . access money\n",
      "       . prepaid card\n",
      "# 'Student loan':\n",
      "  . Most correlated unigrams:\n",
      "       . student\n",
      "       . navient\n",
      "  . Most correlated bigrams:\n",
      "       . student loans\n",
      "       . student loan\n",
      "# 'Virtual currency':\n",
      "  . Most correlated unigrams:\n",
      "       . handles\n",
      "       . https\n",
      "  . Most correlated bigrams:\n",
      "       . xxxx provider\n",
      "       . money want\n"
     ]
    }
   ],
   "source": [
    "from sklearn.feature_selection import chi2\n",
    "import numpy as np\n",
    "\n",
    "N = 2\n",
    "for Product, category_id in sorted(category_to_id.items()):\n",
    "  features_chi2 = chi2(features, labels == category_id)\n",
    "  indices = np.argsort(features_chi2[0])\n",
    "  feature_names = np.array(tfidf.get_feature_names())[indices]\n",
    "  unigrams = [v for v in feature_names if len(v.split(' ')) == 1]\n",
    "  bigrams = [v for v in feature_names if len(v.split(' ')) == 2]\n",
    "  print(\"# '{}':\".format(Product))\n",
    "  print(\"  . Most correlated unigrams:\\n       . {}\".format('\\n       . '.join(unigrams[-N:])))\n",
    "  print(\"  . Most correlated bigrams:\\n       . {}\".format('\\n       . '.join(bigrams[-N:])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.feature_extraction.text import TfidfTransformer\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(df['Consumer_complaint_narrative'], df['Product'], random_state = 0)\n",
    "count_vect = CountVectorizer()\n",
    "X_train_counts = count_vect.fit_transform(X_train)\n",
    "tfidf_transformer = TfidfTransformer()\n",
    "X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)\n",
    "\n",
    "clf = MultinomialNB().fit(X_train_tfidf, y_train)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Debt collection']\n"
     ]
    }
   ],
   "source": [
    "print(clf.predict(count_vect.transform([\"This company refuses to provide me verification and validation of debt per my right under the FDCPA. I do not believe this debt is mine.\"])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Credit reporting']\n"
     ]
    }
   ],
   "source": [
    "print(clf.predict(count_vect.transform([\"I am disputing the inaccurate information the Chex-Systems has on my credit report. I initially submitted a police report on XXXX/XXXX/16 and Chex Systems only deleted the items that I mentioned in the letter and not all the items that were actually listed on the police report. In other words they wanted me to say word for word to them what items were fraudulent. The total disregard of the police report and what accounts that it states that are fraudulent. If they just had paid a little closer attention to the police report I would not been in this position now and they would n't have to research once again. I would like the reported information to be removed : XXXX XXXX XXXX\"])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>Consumer_complaint_narrative</th>\n",
       "      <th>category_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>This company refuses to provide me verificatio...</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Product                       Consumer_complaint_narrative  \\\n",
       "12  Debt collection  This company refuses to provide me verificatio...   \n",
       "\n",
       "    category_id  \n",
       "12            2  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['Consumer_complaint_narrative'] == \"This company refuses to provide me verification and validation of debt per my right under the FDCPA. I do not believe this debt is mine.\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>Consumer_complaint_narrative</th>\n",
       "      <th>category_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>61</th>\n",
       "      <td>Credit reporting</td>\n",
       "      <td>I am disputing the inaccurate information the ...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Product                       Consumer_complaint_narrative  \\\n",
       "61  Credit reporting  I am disputing the inaccurate information the ...   \n",
       "\n",
       "    category_id  \n",
       "61            0  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['Consumer_complaint_narrative'] == \"I am disputing the inaccurate information the Chex-Systems has on my credit report. I initially submitted a police report on XXXX/XXXX/16 and Chex Systems only deleted the items that I mentioned in the letter and not all the items that were actually listed on the police report. In other words they wanted me to say word for word to them what items were fraudulent. The total disregard of the police report and what accounts that it states that are fraudulent. If they just had paid a little closer attention to the police report I would not been in this position now and they would n't have to research once again. I would like the reported information to be removed : XXXX XXXX XXXX\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/ec2-user/anaconda3/envs/python3/lib/python3.6/site-packages/sklearn/model_selection/_split.py:605: Warning: The least populated class in y has only 1 members, which is too few. The minimum number of members in any class cannot be less than n_splits=5.\n",
      "  % (min_groups, self.n_splits)), Warning)\n",
      "/home/ec2-user/anaconda3/envs/python3/lib/python3.6/site-packages/sklearn/model_selection/_split.py:605: Warning: The least populated class in y has only 1 members, which is too few. The minimum number of members in any class cannot be less than n_splits=5.\n",
      "  % (min_groups, self.n_splits)), Warning)\n",
      "/home/ec2-user/anaconda3/envs/python3/lib/python3.6/site-packages/sklearn/model_selection/_split.py:605: Warning: The least populated class in y has only 1 members, which is too few. The minimum number of members in any class cannot be less than n_splits=5.\n",
      "  % (min_groups, self.n_splits)), Warning)\n",
      "/home/ec2-user/anaconda3/envs/python3/lib/python3.6/site-packages/sklearn/model_selection/_split.py:605: Warning: The least populated class in y has only 1 members, which is too few. The minimum number of members in any class cannot be less than n_splits=5.\n",
      "  % (min_groups, self.n_splits)), Warning)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "from sklearn.svm import LinearSVC\n",
    "\n",
    "from sklearn.model_selection import cross_val_score\n",
    "\n",
    "\n",
    "models = [\n",
    "    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),\n",
    "    LinearSVC(),\n",
    "    MultinomialNB(),\n",
    "    LogisticRegression(random_state=0),\n",
    "]\n",
    "CV = 5\n",
    "cv_df = pd.DataFrame(index=range(CV * len(models)))\n",
    "entries = []\n",
    "for model in models:\n",
    "  model_name = model.__class__.__name__\n",
    "  accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV)\n",
    "  for fold_idx, accuracy in enumerate(accuracies):\n",
    "    entries.append((model_name, fold_idx, accuracy))\n",
    "cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7f72cbc4ac50>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "\n",
    "sns.boxplot(x='model_name', y='accuracy', data=cv_df)\n",
    "sns.stripplot(x='model_name', y='accuracy', data=cv_df, \n",
    "              size=8, jitter=True, edgecolor=\"gray\", linewidth=2)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "model_name\n",
       "LinearSVC                 0.822890\n",
       "LogisticRegression        0.792927\n",
       "MultinomialNB             0.688519\n",
       "RandomForestClassifier    0.443826\n",
       "Name: accuracy, dtype: float64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cv_df.groupby('model_name').accuracy.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "model = LinearSVC()\n",
    "\n",
    "X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index, test_size=0.33, random_state=0)\n",
    "model.fit(X_train, y_train)\n",
    "y_pred = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\nIYQQBtL/BxhSpB+n0/QiAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7f72cbc37940>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "\n",
    "conf_mat = confusion_matrix(y_test, y_pred)\n",
    "fig, ax = plt.subplots(figsize=(8,6))\n",
    "sns.heatmap(conf_mat, annot=True, fmt='d',\n",
    "            xticklabels=category_id_df.Product.values, yticklabels=category_id_df.Product.values)\n",
    "plt.ylabel('Actual')\n",
    "plt.xlabel('Predicted')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'Consumer Loan' predicted as 'Credit reporting' : 10 examples.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>Consumer_complaint_narrative</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2720</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>Quoting them, your first loan application, the...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7091</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>While reviewing my XXXX credit report, I notic...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5439</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>I have been recently checking my credit report...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12763</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>We went to buy XXXX cars, and the dealership s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13158</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>I got a 30 day late XX/XX/2017 and it 's repor...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4134</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>I took out an instalment loan in the amount XX...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13848</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>I was turned down for a loan by Honda Finacial...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19227</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>ONEMAIN # XXXX XXXX , IN XXXX ( XXXX ) XXXX Da...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11258</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>I have not been given credit for the payments ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11242</th>\n",
       "      <td>Consumer Loan</td>\n",
       "      <td>Reliable Credit falsely submitted an applicati...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Product                       Consumer_complaint_narrative\n",
       "2720   Consumer Loan  Quoting them, your first loan application, the...\n",
       "7091   Consumer Loan  While reviewing my XXXX credit report, I notic...\n",
       "5439   Consumer Loan  I have been recently checking my credit report...\n",
       "12763  Consumer Loan  We went to buy XXXX cars, and the dealership s...\n",
       "13158  Consumer Loan  I got a 30 day late XX/XX/2017 and it 's repor...\n",
       "4134   Consumer Loan  I took out an instalment loan in the amount XX...\n",
       "13848  Consumer Loan  I was turned down for a loan by Honda Finacial...\n",
       "19227  Consumer Loan  ONEMAIN # XXXX XXXX , IN XXXX ( XXXX ) XXXX Da...\n",
       "11258  Consumer Loan  I have not been given credit for the payments ...\n",
       "11242  Consumer Loan  Reliable Credit falsely submitted an applicati..."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "'Debt collection' predicted as 'Credit reporting' : 18 examples.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>Consumer_complaint_narrative</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>18410</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>Dear CFPB, I am asking you for assistance to i...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5262</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>XXXX XXXX, XXXX ( This letter describes in det...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11834</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>XXXX XXXX XXXX is reporting negatively on my c...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19652</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>I recently paid of both debts on my credit acc...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15557</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>Never have been a XXXX XXXX customer. I was at...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4431</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>someone tried getting credit information and i...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15949</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>This debt is from account from $ XX/XX/2008 an...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12475</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>In XXXX XXXX, there was an account opened thro...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13548</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>DIVERSIFIELD CONSULTANTS INC HAVE VIOLATED FCR...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6988</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>Also collections refuses to stop reporting to ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16498</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>They called my son and told him that they are ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12028</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>Rubin &amp; Rothman LLC ( R &amp; R ) received default...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7131</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>THIS IS FRAUD. I HAVE REQUESTED VERIFICATION A...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15630</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>Barclays Bank Delaware obtained a judgment aga...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11112</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>This account was a joint account with XXXX and...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>This complaint is in regards to Square Two Fin...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>311</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>Hunter Warfield has be unable to provide prope...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15988</th>\n",
       "      <td>Debt collection</td>\n",
       "      <td>Unknown account, never have been notified and ...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Product                       Consumer_complaint_narrative\n",
       "18410  Debt collection  Dear CFPB, I am asking you for assistance to i...\n",
       "5262   Debt collection  XXXX XXXX, XXXX ( This letter describes in det...\n",
       "11834  Debt collection  XXXX XXXX XXXX is reporting negatively on my c...\n",
       "19652  Debt collection  I recently paid of both debts on my credit acc...\n",
       "15557  Debt collection  Never have been a XXXX XXXX customer. I was at...\n",
       "4431   Debt collection  someone tried getting credit information and i...\n",
       "15949  Debt collection  This debt is from account from $ XX/XX/2008 an...\n",
       "12475  Debt collection  In XXXX XXXX, there was an account opened thro...\n",
       "13548  Debt collection  DIVERSIFIELD CONSULTANTS INC HAVE VIOLATED FCR...\n",
       "6988   Debt collection  Also collections refuses to stop reporting to ...\n",
       "16498  Debt collection  They called my son and told him that they are ...\n",
       "12028  Debt collection  Rubin & Rothman LLC ( R & R ) received default...\n",
       "7131   Debt collection  THIS IS FRAUD. I HAVE REQUESTED VERIFICATION A...\n",
       "15630  Debt collection  Barclays Bank Delaware obtained a judgment aga...\n",
       "11112  Debt collection  This account was a joint account with XXXX and...\n",
       "16     Debt collection  This complaint is in regards to Square Two Fin...\n",
       "311    Debt collection  Hunter Warfield has be unable to provide prope...\n",
       "15988  Debt collection  Unknown account, never have been notified and ..."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "'Mortgage' predicted as 'Credit reporting' : 6 examples.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>Consumer_complaint_narrative</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4637</th>\n",
       "      <td>Mortgage</td>\n",
       "      <td>This complaint is in follow-up to Complaint # ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5269</th>\n",
       "      <td>Mortgage</td>\n",
       "      <td>The attached complaint was initially written t...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7343</th>\n",
       "      <td>Mortgage</td>\n",
       "      <td>In 2014, I went to XXXX in order to buy a mobi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15048</th>\n",
       "      <td>Mortgage</td>\n",
       "      <td>Company repeatedly corrects my credit report a...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>861</th>\n",
       "      <td>Mortgage</td>\n",
       "      <td>Mortgage broker did Credit inquiry on my credi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19781</th>\n",
       "      <td>Mortgage</td>\n",
       "      <td>I am a card carrying XXXX and wanted to see if...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Product                       Consumer_complaint_narrative\n",
       "4637   Mortgage  This complaint is in follow-up to Complaint # ...\n",
       "5269   Mortgage  The attached complaint was initially written t...\n",
       "7343   Mortgage  In 2014, I went to XXXX in order to buy a mobi...\n",
       "15048  Mortgage  Company repeatedly corrects my credit report a...\n",
       "861    Mortgage  Mortgage broker did Credit inquiry on my credi...\n",
       "19781  Mortgage  I am a card carrying XXXX and wanted to see if..."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "'Credit card' predicted as 'Credit reporting' : 9 examples.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>Consumer_complaint_narrative</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>18643</th>\n",
       "      <td>Credit card</td>\n",
       "      <td>I was told this account wiuld be deleted from ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18574</th>\n",
       "      <td>Credit card</td>\n",
       "      <td>This inquiry was n't me</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19868</th>\n",
       "      <td>Credit card</td>\n",
       "      <td>Capital One/Kohls has been reporting a past du...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19963</th>\n",
       "      <td>Credit card</td>\n",
       "      <td>on XX/XX/XXXX my wallet was stolen with all my...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4706</th>\n",
       "      <td>Credit card</td>\n",
       "      <td>American Express is reporting an account on my...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21566</th>\n",
       "      <td>Credit card</td>\n",
       "      <td>Have disputed the reporting of the status of a...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13906</th>\n",
       "      <td>Credit card</td>\n",
       "      <td>I have been the victim of identity theft fraud...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16853</th>\n",
       "      <td>Credit card</td>\n",
       "      <td>I have requested XXXX XXXX to run a credit rep...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10505</th>\n",
       "      <td>Credit card</td>\n",
       "      <td>I have been working since XXXX 2016 to get a i...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Product                       Consumer_complaint_narrative\n",
       "18643  Credit card  I was told this account wiuld be deleted from ...\n",
       "18574  Credit card                            This inquiry was n't me\n",
       "19868  Credit card  Capital One/Kohls has been reporting a past du...\n",
       "19963  Credit card  on XX/XX/XXXX my wallet was stolen with all my...\n",
       "4706   Credit card  American Express is reporting an account on my...\n",
       "21566  Credit card  Have disputed the reporting of the status of a...\n",
       "13906  Credit card  I have been the victim of identity theft fraud...\n",
       "16853  Credit card  I have requested XXXX XXXX to run a credit rep...\n",
       "10505  Credit card  I have been working since XXXX 2016 to get a i..."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "index 11 is out of bounds for axis 0 with size 11",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-22-9932ab8bdc5b>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mpredicted\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mcategory_id_df\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcategory_id\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m   \u001b[0;32mfor\u001b[0m \u001b[0mactual\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mcategory_id_df\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcategory_id\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m     \u001b[0;32mif\u001b[0m \u001b[0mpredicted\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mactual\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mconf_mat\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mactual\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpredicted\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m>=\u001b[0m \u001b[0;36m6\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m       \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"'{}' predicted as '{}' : {} examples.\"\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mid_to_category\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mactual\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mid_to_category\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mpredicted\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconf_mat\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mactual\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpredicted\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m       \u001b[0mdisplay\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mloc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mindices_test\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my_test\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mactual\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m&\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0my_pred\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mpredicted\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Product'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'Consumer_complaint_narrative'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mIndexError\u001b[0m: index 11 is out of bounds for axis 0 with size 11"
     ]
    }
   ],
   "source": [
    "from IPython.display import display\n",
    "\n",
    "for predicted in category_id_df.category_id:\n",
    "  for actual in category_id_df.category_id:\n",
    "    if predicted != actual and conf_mat[actual, predicted] >= 6:\n",
    "      print(\"'{}' predicted as '{}' : {} examples.\".format(id_to_category[actual], id_to_category[predicted], conf_mat[actual, predicted]))\n",
    "      display(df.loc[indices_test[(y_test == actual) & (y_pred == predicted)]][['Product', 'Consumer_complaint_narrative']])\n",
    "      print('')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,\n",
       "     intercept_scaling=1, loss='squared_hinge', max_iter=1000,\n",
       "     multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,\n",
       "     verbose=0)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(features, labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "# 'Bank account or service':\n",
      "  . Top unigrams:\n",
      "       . bank\n",
      "       . account\n",
      "  . Top bigrams:\n",
      "       . debit card\n",
      "       . overdraft fees\n",
      "# 'Consumer Loan':\n",
      "  . Top unigrams:\n",
      "       . vehicle\n",
      "       . car\n",
      "  . Top bigrams:\n",
      "       . personal loan\n",
      "       . history xxxx\n",
      "# 'Credit card':\n",
      "  . Top unigrams:\n",
      "       . card\n",
      "       . discover\n",
      "  . Top bigrams:\n",
      "       . credit card\n",
      "       . discover card\n",
      "# 'Credit reporting':\n",
      "  . Top unigrams:\n",
      "       . equifax\n",
      "       . transunion\n",
      "  . Top bigrams:\n",
      "       . xxxx account\n",
      "       . trans union\n",
      "# 'Debt collection':\n",
      "  . Top unigrams:\n",
      "       . debt\n",
      "       . collection\n",
      "  . Top bigrams:\n",
      "       . account credit\n",
      "       . time provided\n",
      "# 'Money transfers':\n",
      "  . Top unigrams:\n",
      "       . paypal\n",
      "       . transfer\n",
      "  . Top bigrams:\n",
      "       . money transfer\n",
      "       . send money\n",
      "# 'Mortgage':\n",
      "  . Top unigrams:\n",
      "       . mortgage\n",
      "       . escrow\n",
      "  . Top bigrams:\n",
      "       . loan modification\n",
      "       . mortgage company\n",
      "# 'Other financial service':\n",
      "  . Top unigrams:\n",
      "       . passport\n",
      "       . dental\n",
      "  . Top bigrams:\n",
      "       . stated pay\n",
      "       . help pay\n",
      "# 'Payday loan':\n",
      "  . Top unigrams:\n",
      "       . payday\n",
      "       . loan\n",
      "  . Top bigrams:\n",
      "       . payday loan\n",
      "       . pay day\n",
      "# 'Prepaid card':\n",
      "  . Top unigrams:\n",
      "       . prepaid\n",
      "       . serve\n",
      "  . Top bigrams:\n",
      "       . prepaid card\n",
      "       . use card\n",
      "# 'Student loan':\n",
      "  . Top unigrams:\n",
      "       . navient\n",
      "       . loans\n",
      "  . Top bigrams:\n",
      "       . student loan\n",
      "       . sallie mae\n",
      "# 'Virtual currency':\n",
      "  . Top unigrams:\n",
      "       . https\n",
      "       . tx\n",
      "  . Top bigrams:\n",
      "       . money want\n",
      "       . xxxx provider\n"
     ]
    }
   ],
   "source": [
    "from sklearn.feature_selection import chi2\n",
    "\n",
    "N = 2\n",
    "for Product, category_id in sorted(category_to_id.items()):\n",
    "  indices = np.argsort(model.coef_[category_id])\n",
    "  feature_names = np.array(tfidf.get_feature_names())[indices]\n",
    "  unigrams = [v for v in reversed(feature_names) if len(v.split(' ')) == 1][:N]\n",
    "  bigrams = [v for v in reversed(feature_names) if len(v.split(' ')) == 2][:N]\n",
    "  print(\"# '{}':\".format(Product))\n",
    "  print(\"  . Top unigrams:\\n       . {}\".format('\\n       . '.join(unigrams)))\n",
    "  print(\"  . Top bigrams:\\n       . {}\".format('\\n       . '.join(bigrams)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\"I requested a home loan modification through Bank of America. Bank of America never got back to me.\"\n",
      "  - Predicted as: 'Mortgage'\n",
      "\n",
      "\"It has been difficult for me to find my past due balance. I missed a regular monthly payment\"\n",
      "  - Predicted as: 'Credit reporting'\n",
      "\n",
      "\"I can't get the money out of the country.\"\n",
      "  - Predicted as: 'Bank account or service'\n",
      "\n",
      "\"I have no money to pay my tuition\"\n",
      "  - Predicted as: 'Debt collection'\n",
      "\n",
      "\"Coinbase closed my account for no reason and furthermore refused to give me a reason despite dozens of request\"\n",
      "  - Predicted as: 'Bank account or service'\n",
      "\n"
     ]
    }
   ],
   "source": [
    "texts = [\"I requested a home loan modification through Bank of America. Bank of America never got back to me.\",\n",
    "         \"It has been difficult for me to find my past due balance. I missed a regular monthly payment\",\n",
    "         \"I can't get the money out of the country.\",\n",
    "         \"I have no money to pay my tuition\",\n",
    "         \"Coinbase closed my account for no reason and furthermore refused to give me a reason despite dozens of request\"]\n",
    "text_features = tfidf.transform(texts)\n",
    "predictions = model.predict(text_features)\n",
    "for text, predicted in zip(texts, predictions):\n",
    "  print('\"{}\"'.format(text))\n",
    "  print(\"  - Predicted as: '{}'\".format(id_to_category[predicted]))\n",
    "  print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                         precision    recall  f1-score   support\n",
      "\n",
      "       Credit reporting       0.82      0.82      0.82       288\n",
      "          Consumer Loan       0.83      0.60      0.70       100\n",
      "        Debt collection       0.80      0.91      0.85       359\n",
      "               Mortgage       0.90      0.93      0.92       317\n",
      "            Credit card       0.73      0.77      0.75       165\n",
      "Other financial service       0.00      0.00      0.00         1\n",
      "Bank account or service       0.74      0.74      0.74       121\n",
      "           Student loan       0.92      0.83      0.87       111\n",
      "        Money transfers       0.50      0.23      0.32        13\n",
      "            Payday loan       0.75      0.38      0.50        16\n",
      "           Prepaid card       0.67      0.12      0.20        17\n",
      "\n",
      "            avg / total       0.82      0.82      0.81      1508\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/ec2-user/anaconda3/envs/python3/lib/python3.6/site-packages/sklearn/metrics/classification.py:1428: UserWarning: labels size, 11, does not match size of target_names, 12\n",
      "  .format(len(labels), len(target_names))\n",
      "/home/ec2-user/anaconda3/envs/python3/lib/python3.6/site-packages/sklearn/metrics/classification.py:1135: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples.\n",
      "  'precision', 'predicted', average, warn_for)\n"
     ]
    }
   ],
   "source": [
    "from sklearn import metrics\n",
    "print(metrics.classification_report(y_test, y_pred, \n",
    "                                    target_names=df['Product'].unique()))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (Spyder)",
   "language": "python3",
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
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}