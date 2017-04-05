## 多対多テーブルに対するSQLの発行例

```sql
BEGIN;
--
-- Create model Article
--
CREATE TABLE "model_sample_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(256) NOT NULL, "text" text NOT NULL);
--
-- Create model ArticleTag
--
CREATE TABLE "model_sample_articletag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "create_date_time" datetime NOT NULL, "article_id" integer NOT NULL REFERENCES "model_sample_article" ("id"));
--
-- Create model Tag
--
CREATE TABLE "model_sample_tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(256) NOT NULL);
--
-- Add field tag to articletag
--
ALTER TABLE "model_sample_articletag" RENAME TO "model_sample_articletag__old";
CREATE TABLE "model_sample_articletag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "create_date_time" datetime NOT NULL, "article_id" integer NOT NULL REFERENCES "model_sample_article" ("id"), "tag_id" integer NOT NULL REFERENCES "model_sample_tag" ("id"));
INSERT INTO "model_sample_articletag" ("article_id", "tag_id", "create_date_time", "id") SELECT "article_id", NULL, "create_date_time", "id" FROM "model_sample_articletag__old";
DROP TABLE "model_sample_articletag__old";
CREATE INDEX "model_sample_articletag_a00c1b00" ON "model_sample_articletag" ("article_id");
CREATE INDEX "model_sample_articletag_76f094bc" ON "model_sample_articletag" ("tag_id");
COMMIT;
```
