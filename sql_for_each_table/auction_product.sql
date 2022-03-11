-- Table: public.auction_product

-- DROP TABLE IF EXISTS public.auction_product;

CREATE TABLE IF NOT EXISTS public.auction_product
(
    id bigint NOT NULL DEFAULT nextval('auction_product_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    base_price double precision NOT NULL,
    current_price double precision NOT NULL,
    current_bidder character varying(20) COLLATE pg_catalog."default",
    "listedBy_id" bigint NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    category character varying(50) COLLATE pg_catalog."default",
    upload_date date NOT NULL,
    last_bid_date date NOT NULL,
    image1 character varying(100) COLLATE pg_catalog."default" NOT NULL,
    image2 character varying(100) COLLATE pg_catalog."default" NOT NULL,
    image3 character varying(100) COLLATE pg_catalog."default" NOT NULL,
    image4 character varying(100) COLLATE pg_catalog."default" NOT NULL,
    image5 character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "isUpcoming" boolean NOT NULL,
    "isOngoing" boolean NOT NULL,
    "isSold" boolean NOT NULL,
    CONSTRAINT auction_product_pkey PRIMARY KEY (id),
    CONSTRAINT "auction_product_listedBy_id_0d5a0465_fk_account_account_id" FOREIGN KEY ("listedBy_id")
        REFERENCES public.account_account (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auction_product
    OWNER to artoction;
-- Index: auction_product_listedBy_id_0d5a0465

-- DROP INDEX IF EXISTS public."auction_product_listedBy_id_0d5a0465";

CREATE INDEX IF NOT EXISTS "auction_product_listedBy_id_0d5a0465"
    ON public.auction_product USING btree
    ("listedBy_id" ASC NULLS LAST)
    TABLESPACE pg_default;