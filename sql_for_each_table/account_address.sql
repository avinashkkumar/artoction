-- Table: public.account_address

-- DROP TABLE IF EXISTS public.account_address;

CREATE TABLE IF NOT EXISTS public.account_address
(
    id bigint NOT NULL DEFAULT nextval('account_address_id_seq'::regclass),
    address_line_one character varying(75) COLLATE pg_catalog."default" NOT NULL,
    address_line_two character varying(75) COLLATE pg_catalog."default" NOT NULL,
    address_line_three character varying(75) COLLATE pg_catalog."default" NOT NULL,
    address_line_four character varying(75) COLLATE pg_catalog."default" NOT NULL,
    address_proof character varying(100) COLLATE pg_catalog."default" NOT NULL,
    is_verified boolean NOT NULL,
    is_deneyed boolean NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT account_address_pkey PRIMARY KEY (id),
    CONSTRAINT "account_address_User_id_key" UNIQUE (user_id),
    CONSTRAINT account_address_user_id_a1553eba_fk_account_account_id FOREIGN KEY (user_id)
        REFERENCES public.account_account (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.account_address
    OWNER to artoction;