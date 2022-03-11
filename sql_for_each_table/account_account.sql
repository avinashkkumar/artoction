-- Table: public.account_account

-- DROP TABLE IF EXISTS public.account_account;

CREATE TABLE IF NOT EXISTS public.account_account
(
    id bigint NOT NULL DEFAULT nextval('account_account_id_seq'::regclass),
    password character varying(128) COLLATE pg_catalog."default" NOT NULL,
    email character varying(60) COLLATE pg_catalog."default" NOT NULL,
    username character varying(30) COLLATE pg_catalog."default" NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_admin boolean NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    is_superuser boolean NOT NULL,
    profile_image character varying(255) COLLATE pg_catalog."default",
    hide_email boolean NOT NULL,
    "firstName" character varying(20) COLLATE pg_catalog."default",
    "lastName" character varying(20) COLLATE pg_catalog."default",
    verified_address boolean NOT NULL,
    CONSTRAINT account_account_pkey PRIMARY KEY (id),
    CONSTRAINT account_account_email_key UNIQUE (email),
    CONSTRAINT account_account_username_key UNIQUE (username)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.account_account
    OWNER to artoction;
-- Index: account_account_email_3d3b3e7a_like

-- DROP INDEX IF EXISTS public.account_account_email_3d3b3e7a_like;

CREATE INDEX IF NOT EXISTS account_account_email_3d3b3e7a_like
    ON public.account_account USING btree
    (email COLLATE pg_catalog."default" varchar_pattern_ops ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: account_account_username_7d6d7da7_like

-- DROP INDEX IF EXISTS public.account_account_username_7d6d7da7_like;

CREATE INDEX IF NOT EXISTS account_account_username_7d6d7da7_like
    ON public.account_account USING btree
    (username COLLATE pg_catalog."default" varchar_pattern_ops ASC NULLS LAST)
    TABLESPACE pg_default; 
