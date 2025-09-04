# git init    "ایجاد گیت"

# file .gitignore    "فایل هایی که در گیت نباشد"

# git add .    git test.py    "ادد کردن به استیج"

# git commit -m "commit 1"    "کامیت در ریپزیتوری"

# git commit -am "commit 87"      "ادد و کامیت "

# git log   git log --oneline    "کامیت ها "

# git branch    "برنچ ها "

# git branch bugfix    "برنچ جدید "

# git switch bugfix    "سویچ به برنچ"

# git switch -c bugfix2    "ایجاد و سویچ به برنچ"

# git log --all --graph   "به صورت گرافیکی"

# git branch -m bugfix3 "تغییر نام برنچ"

# git branch -d bugfix3        git branch -D bugfix3   "دلیت برنچ"

# git merge bugfix      "باید در برنچ مستر باشیم که برنچ باگ فیسک به برنچ مستر مرچ شود"

# git diff     "تغییرات ورکینگ دایرکتوری ادیتور با استیجین اریا"

# git diff --staged      "استیجین اریا با اخرین کامیت"

# git diff HEAD     "تغییرات ورکینگ دایرکتوری ادیتور با اخرین کامیت"

# git diff commit1..commit2          "تغییرات بین دو کامیت با هش بنویس"

# git diff branch1..branch2          "تغییرات بین دو برنچ با اسم بنویس"

# git checkout commit7          "بازگشت به یک کامیت خاص و با هش بنویس"
# git switch master          "بازگشت به کامیت اخر مستر "
# git checkout HEAD        "بازگشت به کامیتی که هد است "
# git checkout HEAD~2      "بازگشت به کامیتی که 2 تا از هد پایین تر است "
# git checkout HEAD file2.py      "پاک کردن تغییراات فایل 2 که هنوز کامیت نشده و ادد نشده "

# git restore file1.py                 "تغییرات ورکینگ دایرکتوری ادیتور فایل 1 را پاک می کند "

# git restore --staged file1.py          "فایل 1 را از استیج خارج می کند "

# git restore --source 9fh2584o7 file1.py      git restore --source HEAD~2 file1.py    "فایل 1 را به ان کامیت تغییر دادن "

# git reset 8e5847n80y    "حذف کردن کامیت ها تا کامیت مشخص شده فقط کامیت"

# git reset --hard 8i2m45o     "حذف کردن کامیت هاو همچنین ورکینگ دایکتوری ان ها تا کامیت مشخص شده"

# git revert 854l236ot          "از کامیت مشخص شده یک کامیت جدید ایجاد می شود و تغییرات و تداخل های کامیت های جلویی را بر طرف می کنیم و کامیت جدید ایجاد می شود "
# git add .          git revert --continue         "در ادامه ریورت باید بزنیم "

# git stash save       git stash save "stash 1"    "تغییرات ورکینگ دایرکتوری را دخیره کردن در یک محفظه"
# git stash pop      "بر گردادندن تغییراتی که در ستش دخیره شده بود و حذف ستش"
# git stash apply    "برگرداندن تغییراتی که در ستش ذخیره شده بود به طوری که ستش حذف نشود "
# git stash list                "لیست ستش ها "
# git stash apply stash@{2}     "برگرداندن تغییراتی که در این ستش وجود دارد "
# git stash drop stash@{2}    "پاک کردن این ستش "
# git stash clear             "پاک کردن کل ستش ها "

# git clone <url site>      "پروزه گیتاب که خواسیتم را بیاوریم "

# git remote               "نمایش ریموت ها یا مقصد ها "

# git remote -v            "نمایش ریموت ها و مقصد هایشان "

# git remote add <name> <url>      "اتصال ریپزیتوری گیت به ریپزیتوری گیت هاب یا مقصد ریپریتوری گیت به ریپریتوری گیت هاب "

# git push <remote> <branch>         git push      "ریپزیتوری که در لوکال داریم را پوش کنیم در گیت هاب "

# git branch -r          "origin/master"  "نمایش ریموت برنچ ها که وظیفه ان ها این است یک پوینتر است که نشان دهنده اخرین کامیتی است که پوش شده "

# git switch <branch99>     "origin/branch99"    "اگر از گیتاب هاب یک پروز اوردیم با دستور گیت سیتچ برنچ دلخواه می توانیم به برنچ های داخل اورجین/برنچ سویتچ کرد "

# git fetch <remote>            git fetch <remote> <branch>         "برگرداندن کامیت ها یا تغییرات جدید که همکار ها داخل گیتهاب اورده اند به لوکال ریپزیتوری سیستم خود "
# git checkout origin/master     "هد را به کامیت بالایی بردن "
# git pull <remote:origin>  <branch:master>        git pull       "برگرداندن کامیت ها و تغییرات جدید که همکار ها داخل گیت هاب اورده اند به ورکینگ دایرکتوری واینکه پول کل و اصلی است اما فتچ بیشتر برای بررسی تداخل است"
